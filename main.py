#!/usr/bin/env python3

import argparse
import sys

import modules.deckbuilder as builder
import modules.nrdb as nrdb

MAX_ICE = 30

def main():
    args = parse_arguments()

    # Sanity checks on optional parameters
    min_ice = args['minimum_ice']
    if min_ice < 0 or min_ice > MAX_ICE:
        error_msg = f'ERROR: Minimum number of ice must be between 0 and {MAX_ICE}'
        die(error_msg)

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
    parser.add_argument('--guaranteed-types', action='store_true',
                        help='guarantee that each deck has all three main types of ice/breakers')
    parser.add_argument('--minimum-ice', type=int, default=0,
                        help='guarantee that each corp deck has at least <number> ice (default is 0)')

    args = parser.parse_args()

    return vars(args)

def die(error_msg):
    print(error_msg)
    sys.exit(1)

if __name__ == "__main__":
    main()
