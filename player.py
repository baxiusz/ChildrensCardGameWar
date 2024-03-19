class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def remove_card_from_hand(self, index):
        if 0 <= index < len(self.hand):
            return self.hand.pop(index)
        else:
            return None

    def get_hand_size(self):
        return len(self.hand)

    def __str__(self):
        return f"Player: {self.name}, Hand: {self.hand}"
