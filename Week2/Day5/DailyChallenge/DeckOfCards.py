import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


class DeckOfCards:
    def __init__(self):
        self.cards = []
        self.populate()

    def populate(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __str__(self):
        return "\n".join([str(card) for card in self.cards])

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if not self.cards:
            return None
        else:
            return self.cards.pop()


deck = DeckOfCards()
deck.shuffle()
print("Deck after shuffling:")
for card in deck.cards:
    print(card)
print("-------")
print("Dealing a card:")
dealt_card = deck.deal()
print("Dealt card:", dealt_card)
print("-------")
print("Remaining cards in the deck:")
for card in deck.cards:
    print(card)
