#!/usr/bin/env python3

import argparse

import modules.deckbuilder as builder
import modules.nrdb as nrdb

def main():
    args = parse_arguments()

    card_pool = nrdb.construct_card_pool()

    side_cards = [ c for c in card_pool if c['side_code'] == args['side'] ]
    deck = builder.generate_deck(args['side'], side_cards)

    print(deck)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate random decks for Android: Netrunner.")

    # Required Args
    parser.add_argument('--side', required=True, choices=['runner', 'corp'])

    args = parser.parse_args()

    return vars(args)

if __name__ == "__main__":
    main()
