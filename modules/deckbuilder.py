import random

from classes.Deck import Deck, CorpDeck

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
    # Select an identity
    identities = [ i for i in card_pool if i['type_code'] == 'identity' ]
    random.shuffle(identities)
    identity = identities.pop()

    deck = CorpDeck(identity)

    # Remove agendas and add those to the deck before anything else
    agendas = [ a for a in card_pool if a['type_code'] == 'agenda'
                                     and a['faction_code'] in [identity['faction_code'], 'neutral-corp'] ]

    # Add agendas until we are in our point range
    point_range = deck.agenda_point_range
    while deck.current_agenda_points < point_range[0]:
        random.shuffle(agendas)
        agenda = agendas.pop()
        number_to_add = random.randint(1, agenda['deck_limit'])
        for i in range(number_to_add):
            deck.addAgenda(agenda)

    other_cards = [ c for c in card_pool if c['type_code'] not in ['identity', 'agenda'] ]

    # Keep adding cards as long as minimum size hasn't been reached
    while deck.current_deck_size < deck.min_deck_size:
        random.shuffle(other_cards)
        card = other_cards.pop()
        number_to_add = random.randint(1, card['deck_limit'])
        for i in range(number_to_add):
            deck.addCard(card, card['faction_code'] == deck.identity['faction_code'])

    return deck
