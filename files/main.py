from blackjack import Game

class Process:
    def __init__(self) -> None:
        self.blackjack = Game()
        self.bets = self.blackjack.game.get_bets()

    def view_hands(self) -> None:
        self.blackjack.view_player_hand()
        self.blackjack.view_dealer_hand()

    def game(self) -> None:
        print(f'You can see your bets as follows:\n{self.bets}')
        print('\nFirst card of the players and the dealer!\n')
        
    def first_round(self):
        self.blackjack.first_card()
        for player in self.blackjack.game.get_players():
            if self.blackjack.dealers_card[self.blackjack.dealer][0][0] == 'A' and self.blackjack.game.get_valid_string('Would you like to get insurance? Enter yes or no! ', 'yes', 'no') == 'yes':
                self.blackjack.get_insurance(player, self.bets//2)

    def second_round(self) -> None:
        print('\nFirst 2 cards of the players and the dealer!\n')
        self.blackjack.second_card()
        self.view_hands()
        for player in self.blackjack.game.get_players():
            if self.blackjack.game.get_valid_string(f'Would you like to surrender your cards {player}? Enter yes or no! ', 'yes', 'no') == 'yes':
                self.blackjack.surrendering(player)
            else: self.blackjack.player_hit(player)
        self.blackjack.dealer_hit()
    
if __name__ == '__main__':
    process = Process()
    process.game()
    process.first_round()
    process.view_hands()
    process.second_round()
    process.view_hands()
    print(f'Here are your winnings:\n{process.blackjack.game.get_bets()}')