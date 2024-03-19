import random

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for rank in ranks:
                self.cards.append(f"{rank} of {suit}")

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

# Example usage:
if __name__ == "__main__":
    deck = Deck()
    print("Initial deck:")
    print(deck.cards)
    print()

    deck.shuffle()
    print("Shuffled deck:")
    print(deck.cards)
    print()

    drawn_card = deck.draw_card()
    print("Drawn card:", drawn_card)
    print()

    print("Updated deck after drawing a card:")
    print(deck.cards)
