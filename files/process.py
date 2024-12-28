from blackjack import Blackjack

class Process:
    def __init__(self) -> None:
        self.blackjack = Blackjack()
        self.blackjack.settings()
        self.bets = self.blackjack.get_bets()
        self.dealer = self.blackjack.get_dealer()

    def view_hands(self) -> None:
        self.blackjack.view_player_hand()
        self.blackjack.view_dealer_hand()

    def display_bets(self) -> None:
        print(f'\nYou can see your bets as follows:\n{self.bets}')
        
    def get_one_round(self, deal_first_or_second_card, player_names: list) -> tuple[dict, dict]:
        for player in player_names:
            deal_first_or_second_card(player, self.blackjack.players_cards)
        deal_first_or_second_card(self.dealer, self.blackjack.dealers_card)
        return self.blackjack.players_cards, self.blackjack.dealers_card

    def surrender(self, player_names: list) -> None:
        for player in player_names:
            surrender = self.blackjack.get_valid_string(f'\nWould you like to surrender your cards {player}? Yes, or no? ', 'yes', 'no')
            if surrender == 'yes': self.blackjack.surrender_cards(player)
            else: self.blackjack.hit_player(player)
        self.blackjack.hit_dealer()

    def insurance_against_blackjack(self, player_names: list) -> None:
        for player in player_names:
            if self.blackjack.dealers_card[self.blackjack.get_dealer()][0][0] == 'A':
                insurance = self.blackjack.get_valid_string(f'Would you like to get insurance {player}? Yes or no? ', 'yes', 'no')
                if insurance == 'yes': self.blackjack.get_insurance(player, self.bets[player]//2)
                    
    def check_winnings(self) -> dict:
        winnings = {}
        for player, card_value in self.blackjack.players_cards.items():
            winnings[player] = 0
            if card_value[-1] > 21 or self.blackjack.players_cards[player][-1] <= self.blackjack.dealers_card[self.blackjack.get_dealer()][-1] <= 21:
                    winnings[player] = -self.blackjack.get_bets()[player]
            else:
                winnings[player] += self.blackjack.get_bets()[player]
        return winnings