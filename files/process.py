from blackjack import Game

class Process:
    def __init__(self) -> None:
        self.blackjack = Game()
        self.bets = self.blackjack.game.get_bets()

    def view_hands(self) -> None:
        self.blackjack.view_player_hand()
        self.blackjack.view_dealer_hand()

    def display_bets(self) -> None:
        print(f'You can see your bets as follows:\n{self.bets}')
        
    def first_round(self) -> None:
        self.blackjack.first_card()
        player_names = self.blackjack.game.get_players()
        for player in player_names:
            if self.blackjack.dealers_card[self.blackjack.dealer][0][0] == 'A':
                insurance_yes_or_no = self.blackjack.game.get_valid_string('Would you like to get insurance? Enter yes or no! ', 'yes', 'no')
                if insurance_yes_or_no == 'yes': self.blackjack.get_insurance(player, self.bets//2)

    def second_round(self) -> None:
        self.blackjack.second_card()
        self.view_hands()
        player_names = self.blackjack.game.get_players()
        for player in player_names:
            surrender_yes_or_no = self.blackjack.game.get_valid_string(f'Would you like to surrender your cards {player}? Enter yes, or no! ', 'yes', 'no')
            if surrender_yes_or_no == 'yes': self.blackjack.surrendering(player)
            else: self.blackjack.player_hit(player)
        self.blackjack.dealer_hit()
        
    def result(self):
        for player, card_value in self.blackjack.players_first_two_cards.items():
            if card_value[-1] > 21:
                self.blackjack.game.get_bets()[player] = 0
            elif self.blackjack.dealers_card[self.blackjack.dealer][-1] <= 21 and \
                self.blackjack.players_first_two_cards[player][-1] <= self.blackjack.dealers_card[self.blackjack.dealer][-1]:
                    self.blackjack.game.get_bets()[player] = 0