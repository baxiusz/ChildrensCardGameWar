from deck import Deck
from player import Player

class WarGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.deck = Deck()

    def deal_cards(self):
        self.deck.shuffle()
        while self.deck.get_cards_count() > 0:
            self.player1.add_card_to_hand(self.deck.draw_card())
            self.player2.add_card_to_hand(self.deck.draw_card())

    def play_round(self):
        card1 = self.player1.remove_card_from_hand(0)
        card2 = self.player2.remove_card_from_hand(0)

        print(f"{self.player1.name} plays: {card1}")
        print(f"{self.player2.name} plays: {card2}")

        if self.rank_value(card1) > self.rank_value(card2):
            print(f"{self.player1.name} wins the round!")
            self.player1.add_card_to_hand(card1)
            self.player1.add_card_to_hand(card2)
        elif self.rank_value(card1) < self.rank_value(card2):
            print(f"{self.player2.name} wins the round!")
            self.player2.add_card_to_hand(card1)
            self.player2.add_card_to_hand(card2)
        else:
            print("It's a tie! WAR begins...")
            self.play_war()

    def play_war(self):
        war_cards_player1 = [self.player1.remove_card_from_hand(i) for i in range(3)]
        war_cards_player2 = [self.player2.remove_card_from_hand(i) for i in range(3)]

        if war_cards_player1[-1] is not None and war_cards_player2[-1] is not None:
            print(f"{self.player1.name} plays: FACE-DOWN, FACE-DOWN, FACE-DOWN, {war_cards_player1[-1]}")
            print(f"{self.player2.name} plays: FACE-DOWN, FACE-DOWN, FACE-DOWN, {war_cards_player2[-1]}")

            if self.rank_value(war_cards_player1[-1]) > self.rank_value(war_cards_player2[-1]):
                print(f"{self.player1.name} wins the WAR!")
                self.player1.add_card_to_hand(war_cards_player1[-1])
                self.player1.add_card_to_hand(war_cards_player2[-1])
                for card in war_cards_player1:
                    self.player1.add_card_to_hand(card)
                for card in war_cards_player2:
                    self.player1.add_card_to_hand(card)
            elif self.rank_value(war_cards_player1[-1]) < self.rank_value(war_cards_player2[-1]):
                print(f"{self.player2.name} wins the WAR!")
                self.player2.add_card_to_hand(war_cards_player1[-1])
                self.player2.add_card_to_hand(war_cards_player2[-1])
                for card in war_cards_player1:
                    self.player2.add_card_to_hand(card)
                for card in war_cards_player2:
                    self.player2.add_card_to_hand(card)
            else:
                print("Another tie in the WAR! Another round of WAR begins...")
                self.play_war()
        else:
            print("Not enough cards to continue the WAR!")



    def rank_value(self, card):
        if card is None:
            return -1  # Or any other suitable default value or handling
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        return ranks.index(card.split()[0])


    def determine_winner(self):
        if self.player1.get_hand_size() == 0:
            return self.player2.name
        elif self.player2.get_hand_size() == 0:
            return self.player1.name
        else:
            return None

    def play_game(self):
        self.deal_cards()
        round_count = 1
        while True:
            print(f"Round {round_count}:")
            self.play_round()
            winner = self.determine_winner()
            if winner:
                print(f"\n{winner} wins the game!")
                break
            round_count += 1