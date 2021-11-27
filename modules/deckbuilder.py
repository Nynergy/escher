import random

from classes.Deck import RunnerDeck, CorpDeck

def generate_deck(args, card_pool):
    if args['side'] == 'runner':
        return generate_runner_deck(args, card_pool)
    else:
        return generate_corp_deck(args, card_pool)

def generate_runner_deck(args, card_pool):
    identity = random_identity(card_pool)
    deck = RunnerDeck(identity)

    non_id_cards = [ c for c in card_pool if c['type_code'] != 'identity' ]

    if args['guaranteed_econ']:
        gamble = next(card for card in non_id_cards if card['title'] == 'Sure Gamble')
        non_id_cards.remove(gamble)

        for i in range(gamble['deck_limit']):
            deck.addCard(gamble, False)

    deck = fill_deck(deck, non_id_cards)

    return deck

def random_identity(card_pool):
    identities = [ i for i in card_pool if i['type_code'] == 'identity' ]
    random.shuffle(identities)
    identity = identities.pop()

    return identity

def fill_deck(deck, card_pool):
    # Keep adding cards as long as minimum size hasn't been reached
    while deck.current_deck_size < deck.min_deck_size:
        random.shuffle(card_pool)
        card = card_pool.pop()
        number_to_add = random.randint(1, card['deck_limit'])
        for i in range(number_to_add):
            deck.addCard(card, card['faction_code'] == deck.identity['faction_code'])

    return deck

def generate_corp_deck(args, card_pool):
    identity = random_identity(card_pool)
    deck = CorpDeck(identity)

    # Add agendas to the deck before anything else
    valid_factions = [identity['faction_code'], 'neutral-corp']
    agendas = [ a for a in card_pool if a['type_code'] == 'agenda'
                                     and a['faction_code'] in valid_factions ]
    deck = fill_agendas(deck, agendas)

    other_cards = [ c for c in card_pool if c['type_code'] not in ['identity', 'agenda'] ]

    if args['guaranteed_econ']:
        hedge = next(card for card in other_cards if card['title'] == 'Hedge Fund')
        other_cards.remove(hedge)

        for i in range(hedge['deck_limit']):
            deck.addCard(hedge, False)

    deck = fill_deck(deck, other_cards)

    return deck

def fill_agendas(deck, card_pool):
    # Add agendas until we are in our point range
    point_range = deck.agenda_point_range
    while deck.current_agenda_points < point_range[0]:
        random.shuffle(card_pool)
        agenda = card_pool.pop()
        number_to_add = random.randint(1, agenda['deck_limit'])
        for i in range(number_to_add):
            deck.addAgenda(agenda)

    return deck
