# escher

A random deck generator for Android: Netrunner

------------------------------------------------------------------------------
<p align="center">
    <img src="escher.jpg">
</p>

## What is _escher_?

_escher_ is a command line tool written in Python that utilizes the
[NetrunnerDB](https://netrunnerdb.com) API to randomly generate legal decks for
both sides of the asymmetrical cyberpunk card game Android: Netrunner.

New to Netrunner? You can read all about it at [this
link](https://nisei.net/about/netrunner) :)

## How do I use it?

First, ensure you have the correct libraries installed. _escher_ utilizes the
[requests library](https://docs.python-requests.org/en/latest/), so to install
it you can run the following:

`$ pip install requests`

Depending on the setup of your own Python environments, you may need to install
it in a different manner. Refer to online resources and the requests
documentation for more information on that if you have trouble installing.

Once all the dependencies are met, you can invoke _escher_ with the `main.py`
file in the following way:

`$ ./main.py --side=runner`

In the above command, I specified that I want to generate a runner deck, but you
can also use `corp` to generate a corp deck. The final legal deck will be output
to the command line for you to pipe into a file, or to copy into your
editor/deckbuilder of choice.

At the moment, _escher_ supports generating legal decks for the Standard format,
and outputs the decklists in the format used to build decks on
[Jinteki.net](https://jinteki.net). For more information on the various formats
of Netrunner, visit [this page](https://nisei.net/players/supported-formats/)

## Why does this tool exist?

That's a fair question. Netrunner is a game with a rich and rewarding
deckbuilding system. Carefully crafting decks for your specific meta and testing
them against other carefully crafted decks is a major part of what keeps
Netrunner fun and interesting. Metas are ever-shifting, and clever deckbuilding
can lead to surprising, edge-of-your-seat gameplay.

Despite this, I sometimes feel that I don't want to sit there and methodically
plan out a deck with win conditions, lines of play, and all that
tournament-level nonsense. Sometimes, I just want to shuffle my cards and see
what kind of random bullshittery comes out! Thus, _escher_ was born.

My main goal with this project was to build something that my friend and I could
use to generate silly random decks that had no business existing, and face off
against each other to see what hilarity ensued. In that respect, I think this
project has already proven to be a success. It forces you to work with what
cards you are given, similar to a draft-format deck.

Games are unpredictable, you never know what your opponent may have in their
deck, or what kind of yomi games they may employ to cover up the holes in their
randomly generated game plan.

Overall, use this tool for some fun, nonsensical games of Netrunner. I hope you
enjoy what I've created here, and I hope to continue maintaining it and adding
to its capabilities.

### Plans for this project

- Implement more game formats (Eternal, Startup, etc.)
- Implement more output formats (Octgn, Markdown, etc.)
- Add more fine-grain control of deck generation
  - Users should specify if they automatically want 3x Hedge Fund/Sure Gamble
  - Users should specify if they automatically want all 3 types of breakers/ice
  - Users should be able to set a specific faction to generate a deck for
  - Users should be able to set a specific ID to generate a deck for
  - Etc.
