#!/usr/bin/env python3

import modules.deckbuilder as builder
import modules.nrdb as nrdb

def main():
    card_pool = nrdb.construct_card_pool()
    #runner_cards = [ c for c in card_pool if c['side_code'] == 'runner' ]
    corp_cards = [ c for c in card_pool if c['side_code'] == 'corp' ]

    #runner_deck = builder.generate_runner_deck(runner_cards)
    corp_deck = builder.generate_corp_deck(corp_cards)

    print(corp_deck)

if __name__ == "__main__":
    main()
