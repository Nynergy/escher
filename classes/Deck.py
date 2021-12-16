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
                return False
            self.current_influence += card['faction_cost']

        self.putCardInDeck(card)

        return True

    def putCardInDeck(self, card):
        count = 0 if card['title'] not in self.cards else self.cards[card['title']]
        count += 1
        self.cards[card['title']] = count
        self.current_deck_size += 1

    def jintekiFormat(self):
        id_string = self.identity['title']
        card_string = ""
        for card, count in self.cards.items():
            card_string += f"\n{count} {card}"

        return id_string + card_string

class RunnerDeck(Deck):
    def __init__(self, identity):
        super().__init__(identity)

class CorpDeck(Deck):
    def __init__(self, identity):
        super().__init__(identity)
        self.generateAgendaPointRange()
        self.current_agenda_points = 0

    def generateAgendaPointRange(self):
        base_minimum = 40
        base_range = [18, 19]

        size_diff = self.min_deck_size - base_minimum
        num_ranges_up = size_diff // 5
        range_increase = 2 * num_ranges_up
        new_range = list(map(lambda r: r + range_increase, base_range))

        self.agenda_point_range = new_range

    def addAgenda(self, card):
        if card['faction_cost'] + self.current_influence > self.influence_limit:
            return False
        if card['agenda_points'] + self.current_agenda_points > self.agenda_point_range[1]:
            return False
        self.current_influence += card['faction_cost']
        self.current_agenda_points += card['agenda_points']

        self.putCardInDeck(card)

        return True
