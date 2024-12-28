from base_klasses import Valid, Bet, Player, Dealer, FrenchDeck
from typing import Any
import random

class Blackjack(Valid):
    def __init__(self) -> None:
        self._cards = FrenchDeck()
        self._dealers = Dealer()

    def set_dealer(self) -> None:
        dealer = self.get_valid_number(f'Choose your dealer from {self._dealers.get_options}! ', 0, list(self._dealers.get_options.keys())[-1])
        self.__dealer = self._dealers.get_options[dealer]

    def get_dealer(self) -> str:
        return f'Dealer: {self.__dealer}'
    
    def set_players(self) -> None:
        self.num_players = self.get_valid_number('Enter the number of players from 1 to 4! ', 1, 4)
        self.__players = [player.get_name for player in [Player() for _ in range(self.num_players)]]
        
    def get_players(self) -> list[str]:
        return self.__players
    
    def set_bets(self) -> None:
        self.__bets = [bet.make_bet() for bet in [Bet() for _ in range(self.num_players)]]
        self.__players_bets = dict(zip(self.__players, self.__bets))
    
    def get_bets(self) -> dict:
        return self.__players_bets
    
    def welcome(self) -> None:
        print(f'\nWelcome to game {self.__class__.__name__} {self.get_players()}! ')

    def deal_card(self) -> tuple:
        card = random.choice(list(self._cards._deck))
        self._cards._deck.remove(card)
        return card
    
    def get_dealt_card_value(self, card: tuple[Any, str]) -> int:
        return self._cards._values[card]
    
    def settings(self) -> None:
        self.set_dealer()
        self.set_players()
        self.set_bets()
        self.welcome()
        
class Game:
    def __init__(self) -> None:
        self.game = Blackjack()
        self.game.settings()
        self.dealer = self.game.get_dealer()
        self.players_cards: dict[str, list] = {}
        self.dealers_card: dict[Any, Any] = {}
    
    def deal_cards(self, player_or_dealer: str, dealt_cards: dict) -> None:
        card = self.game.deal_card()
        card_value = self.game.get_dealt_card_value(card)
        dealt_cards[player_or_dealer] = [card, card_value]
        if len(dealt_cards) > 1:
            self.update_card(player_or_dealer, card, dealt_cards)
    
    def update_card(self, player: str, card: tuple, dealt_cards: dict) -> None:
        dealt_cards[player][0] += card
        dealt_cards[player][-1] += self.game.get_dealt_card_value(card)
        if dealt_cards[player][-1] < 10 and card[0] == 'A': dealt_cards[player][-1] += 10
        
    def hit_player(self, player) -> None:
        while self.game.get_valid_string(f'\nDo you want to hit {player}? Enter yes, or no! ', 'yes', 'no') == 'yes':
            card = self.game.deal_card()
            self.update_card(player, card, self.players_cards)
            if self.players_cards[player][-1] > 21:
                print(f'{player} lost! ')
                return
            print(self.players_cards)
            
    def hit_dealer(self) -> None:
        while self.dealers_card[self.dealer][-1] < 16:
            card = self.game.deal_card()
            if self.dealers_card[self.dealer][-1] > 21:
                print(f'{self.dealer} lost! ')
                return
            self.update_card(self.dealer, card, self.dealers_card)
    
    def view_player_hand(self) -> None:
        for player, card_and_value in self.players_cards.items():
            print(player,'->',card_and_value)
    
    def view_dealer_hand(self) -> None:
        for dealer, card_and_value in self.dealers_card.items():
            print(dealer,'->',card_and_value)
    
    def get_insurance(self, player: str, insurance: int) -> None:
        self.game.get_bets()[player] += insurance

    def surrender_cards(self, player: str) -> None:
        self.game.get_bets()[player] *= 0.5