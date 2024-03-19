from game_logic import WarGame

class WarGameUI:
    def __init__(self):
        self.game = WarGame("Player 1", "Player 2")
        self.game.deal_cards()  # Deal cards before starting the game

    def print_intro(self):
        print("Welcome to the War card game!")
        print("Let's start the game...\n")

    def print_players_hand(self):
        print(f"{self.game.player1.name}'s hand: {self.game.player1.hand}")
        print(f"{self.game.player2.name}'s hand: {self.game.player2.hand}\n")

    def print_round_info(self, round_count):
        print(f"Round {round_count}:")
        print(f"{self.game.player1.name}: {len(self.game.player1.hand)} cards")
        print(f"{self.game.player2.name}: {len(self.game.player2.hand)} cards")
        print("")

    def print_round_winner(self, winner):
        print(f"{winner} wins the round!\n")

    def print_game_winner(self, winner):
        print(f"{winner} wins the game!")

    def start_game(self):
        self.print_intro()
        round_count = 1
        while True:
            self.print_round_info(round_count)
            input("Press Enter to play the round...")
            print("")
            self.game.play_round()
            winner = self.game.determine_winner()
            if winner:
                self.print_game_winner(winner)
                break
            round_count += 1

# Example usage:
if __name__ == "__main__":
    ui = WarGameUI()
    ui.start_game()
