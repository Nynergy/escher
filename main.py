#!/usr/bin/env python3

import argparse

import modules.deckbuilder as builder
import modules.nrdb as nrdb

def main():
    args = parse_arguments()

    card_pool = nrdb.construct_card_pool()

    side_cards = [ c for c in card_pool if c['side_code'] == args['side'] ]
    deck = builder.generate_deck(args, side_cards)

    print(deck.jintekiFormat())

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate random decks for Android: Netrunner.")

    # Required Args
    parser.add_argument('--side', required=True, choices=['runner', 'corp'],
                        help='choose a side to generate a deck for')

    # Optional Args
    parser.add_argument('--guaranteed-econ', action='store_true',
                        help='guarantee that each deck has 3x Sure Gamble/Hedge Fund')

    args = parser.parse_args()

    return vars(args)

if __name__ == "__main__":
    main()
