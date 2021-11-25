class Deck:
    def __init__(self, identity):
        self.identity = identity
        self.min_deck_size = identity['minimum_deck_size']
        self.current_deck_size = 0
        self.influence_limit = identity['influence_limit']
        self.current_influence = 0
        self.cards = {}

    def addCard(self, card, in_faction):
        if not in_faction:
            if card['faction_cost'] + self.current_influence > self.influence_limit:
                return
            self.current_influence += card['faction_cost']

        count = 0 if card['stripped_title'] not in self.cards else self.cards[card['stripped_title']]
        count += 1
        self.cards[card['stripped_title']] = count
        self.current_deck_size += 1

    def __str__(self):
        id_string = self.identity['stripped_title']
        card_string = ""
        for card, count in self.cards.items():
            card_string += f"\n{count} {card}"

        return id_string + card_string
