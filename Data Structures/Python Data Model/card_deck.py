import collections

Card = collections.namedtuple("Card", ["rank", "suit"])

card = Card("7", "hearts")
print(len(card))

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = ["spades", "diamonds", "clubs", "hearts"]

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(len(deck)) # returns 52

# __getitem__ also supports slicing
print(deck[:3])

# __getitem__ also supports iteration
for card in deck:
    print(card)

# sorting cards in order of increasing rank
suits_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suits_values) + suits_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
