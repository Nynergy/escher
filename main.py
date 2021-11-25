#!/usr/bin/env python3

import random
import requests

from classes.Deck import Deck

NRDB = 'https://netrunnerdb.com/api/2.0/public/'

def get_from_nrdb(endpoint):
    r = requests.get(NRDB + endpoint)
    data = r.json()['data']

    return data

def main():
    card_pool = construct_card_pool()

    # Runner Deck
    # Select an identity
    identities = [ i for i in card_pool if i['type_code'] == 'identity'
                                        and i['side_code'] == 'runner' ]
    random.shuffle(identities)
    identity = identities.pop()
    deck = Deck(identity)

    runner_cards = [ c for c in card_pool if c['side_code'] == 'runner'
                                          and c['type_code'] != 'identity' ]

    while deck.current_deck_size < deck.min_deck_size:
        random.shuffle(runner_cards)
        card = runner_cards.pop()
        number_to_add = random.randint(1, card['deck_limit'])
        for i in range(number_to_add):
            deck.addCard(card, card['faction_code'] == deck.identity['faction_code'])

    print(deck)

def construct_card_pool():
    all_cards = get_all_cards()
    cycles = get_legal_cycles()
    banlist = get_current_banlist()
    legal_cards = restrict_card_pool(all_cards, cycles, banlist)

    card_pool = []
    for card in legal_cards:
        card_pool.append(card)

    return card_pool

def get_all_cards():
    cards = get_from_nrdb('cards')

    return cards

def get_legal_cycles():
    cycles = get_from_nrdb('cycles')
    illegal_cycles = ['draft', 'napd', 'magnum-opus']
    legal_cycles = [ c['code'] for c in cycles if c['rotated'] == False
                                               and c['code'] not in illegal_cycles ]

    return legal_cycles

def get_current_banlist():
    banlists = get_from_nrdb('mwl')
    current_banlist = [ b for b in banlists if b['active'] == True ][0]
    banned_cards = current_banlist['cards'].keys()

    return banned_cards

def restrict_card_pool(all_cards, cycles, banlist):
    packs = get_from_nrdb('packs')
    code_pairs = map(lambda pack: (pack['code'], pack['cycle_code']), packs)
    code_conversions = { p:c for (p,c) in code_pairs }

    def is_in_rotation(c):
        cycle_code = code_conversions[c['pack_code']]
        
        return cycle_code in cycles

    def is_not_banned(c):
        return c['code'] not in banlist

    in_rotation_cards = [ c for c in all_cards if is_in_rotation(c) ]
    # We also need to ignore neutral IDs from System Gateway
    legal_cards = [ c for c in in_rotation_cards if is_not_banned(c)
                                                 and c['code'] not in ['30076', '30077'] ]

    return legal_cards

if __name__ == "__main__":
    main()
