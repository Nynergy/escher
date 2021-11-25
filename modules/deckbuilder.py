import random

from classes.Deck import Deck

def generate_runner_deck(card_pool):
    # Select an identity
    identities = [ i for i in card_pool if i['type_code'] == 'identity' ]
    random.shuffle(identities)
    identity = identities.pop()

    deck = Deck(identity)

    non_id_cards = [ c for c in card_pool if c['type_code'] != 'identity' ]

    # Keep adding cards as long as minimum size hasn't been reached
    while deck.current_deck_size < deck.min_deck_size:
        random.shuffle(non_id_cards)
        card = non_id_cards.pop()
        number_to_add = random.randint(1, card['deck_limit'])
        for i in range(number_to_add):
            deck.addCard(card, card['faction_code'] == deck.identity['faction_code'])

    return deck

def generate_corp_deck(card_pool):
    return "Corp dekcs not yet implemented"
