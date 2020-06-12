from enum import Enum
from typing import *

import random

class Suit(Enum):
    CLUB    = 1
    DIAMOND = 2
    HEART   = 3
    SPADE   = 4

    def __str__(self):
        return Suit.STRINGS[self.value]

Suit.STRINGS = { 1: "♣", 2: "♦", 3: "♥", 4: "♠"}

class Rank(Enum):
    ACE   = 1
    TWO   = 2
    THREE = 3
    FOUR  = 4
    FIVE  = 5
    SIX   = 6
    SEVEN = 7
    EIGHT = 8
    NINE  = 9
    TEN   = 10
    JACK  = 11
    QUEEN = 12
    KING  = 13

    def __str__(self):
        return Rank.STRINGS[self.value]

    def score(self):  # cannot use value for an enum
        return Rank.SCORES[self.value]

Rank.STRINGS = { 1: "A", 2: "2", 3: "3", 4: "4", 5: "5",
                 6: "6", 7: "7", 8: "8", 9: "9", 10: "10",
                 11: "J", 12: "Q", 13: "K" }
Rank.SCORES = { 1: 10, 2: 2, 3: 3, 4: 4, 5: 5,
                6: 6, 7: 7, 8: 8, 9: 9, 10: 10,
                11: 10, 12: 10, 13: 10 }

class Card:
    def __init__(self, r: Rank, s: Suit):
        self.r = r
        self.s = s

    def __str__(self):
        return "{}{}".format(self.r, self.s)
    def __repr__(self):
        return self.__str__()

    def value(self):
        return self.r.score()

class ListOfCards:
    def __init__(self, l: List[Card] = None):
        if (l is None):
            self.l = []
        else:
            self.l = l

    def __str__(self):
        return str(self.l)

    def __len__(self):
        return len(self.l)

    def is_empty(self):
        return len(self) == 0

class Deck(ListOfCards):
    def shuffle(self):
        random.shuffle(self.l)

    def standard():
        cards = [ Card(r, s) for s in Suit for r in Rank ]
        return Deck(cards)

    def pick(self):
        if self.is_empty():
            raise Exception("No more cards in deck")
        else:
            l = self.l.pop(0)
            return l

# d = Deck.standard()
# print(d)
# d.shuffle()
# print(d)
# print(d.pick())
# print(d)
# d = Deck()
# print(d)
# d.pick()

class Hand(ListOfCards):
    def add(self, c: Card):
        self.l.append(c)

    def value(self):
        return sum(map(lambda c: c.value(), self.l))

# h = Hand()
# print(h)
# h.add(Card(Rank.ACE, Suit.HEART))
# h.add(Card(Rank.TWO, Suit.SPADE))
# print(h)
# print(h.value())

class Player():
    def __init__(self, name: str):
        self.n = name
        self.h = Hand()
        self.active = True

    def __str__(self):
        if (self.h.is_empty()):
            return "{} (no cards, {})".\
                format(self.n,
                       "active" if self.active else "stopped")
        else:
            return "{} ({}, value {}, {})".\
                format(self.n, self.h, self.h.value(),
                       "active" if self.active else "stopped")

    def give_card(self, c: Card):
        self.h.add(c)
        if (self.h.value() > 21):
            self.active = False

    def is_active(self):
        return self.active

    def decide_to_stop_or_not(self): # Abstract method
        pass                         # Implemented in subclasses

# p = Player("Roméo")
# print(p)
# p.give_card(Card(Rank.THREE, Suit.DIAMOND))
# print(p)

class CautiousPlayer(Player):
    def decide_to_stop_or_not(self):
        if (self.h.value() > 11):
            self.active = False

class Dealer(Player):
    def __init__(self, name: str):
        Player.__init__(self, name)
        self.deck = Deck.standard()
        self.deck.shuffle()

    def __str__(self):
        return "{} ({} cards in deck)".format(Player.__str__(self),
                                              len(self.deck))
    def deal(self):
        return self.deck.pick()

    def decide_to_stop_or_not(self):
        if (self.h.value() == 21):
            self.active = False

# d = Dealer("Walter")
# print(d)

class Game():
    def __init__(self, dealer_name: str):
        self.dealer  = Dealer(dealer_name)
        self.players = [ self.dealer ]
        self.turn    = 0

    def add(self, p: Player):
        self.players.append(p)

    def __repr__(self):
        return "Turn : {}\n{}".format(self.turn,
                         "\n".join(map(lambda p: "- " + str(p), self.players)))

    def active_players(self):
        return [p for p in self.players if p.is_active()]

    def deal_cards(self):
        self.turn += 1
        for p in self.players:
            if p.is_active():
                p.give_card(self.dealer.deal())
                p.decide_to_stop_or_not()

    def is_not_finished(self):
        return len(self.active_players()) > 0

    def winner(self):
        if (self.is_not_finished()):
            return None
        else:
            w = max([p for p in self.players if p.h.value() <= 21],
                    key = lambda p: p.h.value())
            print(w)
            return w


g = Game("Walter")
g.add(Player("Roméo"))
g.add(CautiousPlayer("Tango"))
while g.is_not_finished():
    print(g)
    g.deal_cards()
print(g)
print("Winner : {}".format(g.winner()))
