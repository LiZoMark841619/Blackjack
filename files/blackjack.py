from base_klasses import Valid, Bet, Player, Dealer, FrenchDeck
from typing import Any
import random

class Blackjack(Valid):
    def __init__(self) -> None:
        self._cards = FrenchDeck()
        self._dealers = Dealer()
        self.players_cards: dict[str, list] = {}
        self.dealers_card: dict[Any, Any] = {}

    def set_dealer(self) -> None:
        dealer = self.get_valid_number(f'Choose your dealer from {self._dealers.get_options}! ', 0, list(self._dealers.get_options.keys())[-1])
        self.__dealer = self._dealers.get_options[dealer]

    def get_dealer(self) -> str:
        return f'Dealer: {self.__dealer}'
    
    def set_players(self) -> None:
        self.num_players = self.get_valid_number('Enter the number of players from 1 to 4! ', 1, 4)
        self.__players = [player.get_name for player in [Player() for _ in range(self.num_players)]]
        
    def get_players(self) -> list:
        return self.__players
    
    def set_bets(self) -> None:
        self.__bets = [bet.get_bet for bet in [Bet() for _ in range(self.num_players)]]
        self.__players_bets = dict(zip(self.__players, self.__bets))
    
    def get_bets(self) -> dict:
        return self.__players_bets
    
    def welcome(self) -> None:
        print(f'\nWelcome to game {self.__class__.__name__} {self.get_players()}! ')

    def deal_card(self) -> tuple:
        card = random.choice(list(self._cards._deck))
        self._cards._deck.remove(card)
        return card
    
    def get_dealt_card_value(self, card) -> int:
        return self._cards._values[card]
    
    def settings(self) -> None:
        self.set_dealer()
        self.set_players()
        self.set_bets()
        self.welcome()
    
    def deal_cards(self, player_or_dealer: str, dealt_cards: dict) -> None:
        card = self.deal_card()
        card_value = self.get_dealt_card_value(card)
        dealt_cards[player_or_dealer] = [card, card_value]
    
    def update_card(self, player: str, dealt_cards: dict) -> None:
        card = self.deal_card()
        card_value = self.get_dealt_card_value(card)
        dealt_cards[player][0] += card
        dealt_cards[player][-1] += card_value
        if dealt_cards[player][-1] < 10 and card[0] == 'A': dealt_cards[player][-1] += 10
        
    def hit_player(self, player: str) -> None:
        while self.get_valid_string(f'\nDo you want to hit {player}? Enter yes, or no! ', 'yes', 'no') == 'yes':
            self.deal_card()
            self.update_card(player, self.players_cards)
            if self.players_cards[player][-1] > 21:
                print(f'{player}, you lost! ')
                return
            print(self.players_cards)
            
    def hit_dealer(self) -> None:
        dealer = self.get_dealer()
        while self.dealers_card[dealer][-1] < 16:
            self.deal_card()
            if self.dealers_card[dealer][-1] > 21:
                return
            self.update_card(dealer, self.dealers_card)
    
    def view_player_hand(self) -> None:
        for player in self.players_cards: print(player,'->',self.players_cards[player])
    
    def view_dealer_hand(self) -> None:
        for dealer in self.dealers_card: print(dealer,'->',self.dealers_card[dealer])
    
    def get_insurance(self, player: str, insurance: int) -> None:
        self.get_bets()[player] += insurance

    def surrender_cards(self, player: str) -> None:
        self.get_bets()[player] *= 0.5