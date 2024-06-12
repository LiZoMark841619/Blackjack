from blackjack import Game

class Process:
    def __init__(self) -> None:
        self.blackjack = Game()
        self.bets = self.blackjack.game.get_bets()

    def view_hands(self) -> None:
        self.blackjack.view_player_hand()
        self.blackjack.view_dealer_hand()

    def display_bets(self) -> None:
        print(f'\nYou can see your bets as follows:\n{self.bets}')
        
    def get_one_round(self, func_, player_names: list) -> tuple[dict, dict]:
        for player in player_names:
            dealt_cards = self.blackjack.players_cards
            func_(player, dealt_cards)
        dealt_cards = self.blackjack.dealers_card
        func_(self.blackjack.dealer, dealt_cards)
        return self.blackjack.players_cards, self.blackjack.dealers_card

    def surrender(self, player_names: list) -> None:
        for player in player_names:
            surrender = self.blackjack.game.get_valid_string(f'\nWould you like to surrender your cards {player}? Enter yes, or no! ', 'yes', 'no')
            if surrender == 'yes':
                self.blackjack.surrender_cards(player)
            else: 
                self.blackjack.hit_player(player)
        self.blackjack.hit_dealer()

    def insurance_against_blackjack(self, player_names: list) -> None:
        for player in player_names:
            if 'A' in self.blackjack.dealers_card[self.blackjack.dealer][0]:
                insurance = self.blackjack.game.get_valid_string(f'Would you like to get insurance {player}? Enter yes or no! ', 'yes', 'no')
                if insurance == 'yes': 
                    self.blackjack.get_insurance(player, self.bets[player]//2)
                    
    def check_winnings(self) -> dict:
        self.winnings = {}
        for player, card_value in self.blackjack.players_cards.items():
            self.winnings[player] = 0
            if card_value[-1] > 21 or (self.blackjack.dealers_card[self.blackjack.dealer][-1] <= 21 and \
                self.blackjack.players_cards[player][-1] <= self.blackjack.dealers_card[self.blackjack.dealer][-1]):
                    self.winnings[player] = -self.blackjack.game.get_bets()[player]
            else:
                self.winnings[player] += self.blackjack.game.get_bets()[player]
        return self.winnings