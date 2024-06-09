from base_klasses import Valid, Player, Dealer, FrenchDeck
from typing import Any
import random

class Blackjack:
    def __init__(self) -> None:
        self._cards = FrenchDeck()
        self._dealers = Dealer()
        self._valid = Valid()
        chosen_dealer = self._valid.get_valid_number(f'Choose your dealer from {self._dealers.get_options}! ', 0, list(self._dealers.get_options.keys())[-1])
        self.__dealer = self._dealers.get_options[chosen_dealer]
        num_players = self._valid.get_valid_number('Enter the number of players from 1 to 4! ', 1, 4)
        players = [Player() for _ in range(num_players)]
        self.__players = [player.get_player_name for player in players]

    def get_dealer(self) -> str:
        return f'Dealer: {self.__dealer}'
            
    def get_players(self) -> list:
        return self.__players
        
    def welcome(self) -> None:
        print(f'Welcome to game {self.__class__.__name__} {self.get_players()}! ')
    
    def deal_card(self) -> None:
        self.__dealt = random.choice(self._cards._deck)
        self._cards._deck.remove(self.__dealt)

    def get_dealt_card(self) -> tuple:
        return self.__dealt
    
    def get_dealt_card_value(self) -> int:
        return self._cards._values[self.__dealt]

class Game:
    def __init__(self) -> None:
        self.game = Blackjack()
        self.valid = Valid()
        self.welcome = self.game.welcome()
        self.dealer = self.game.get_dealer()
        self.players_first_two_cards: dict[str, list] = {}
        self.dealers_card: dict[Any, Any] = {}

    def first_card(self) -> None:
        for player in self.game.get_players():
            self.game.deal_card()
            self.players_first_two_cards[player] = [self.game.get_dealt_card(), self.game.get_dealt_card_value()]
        self.game.deal_card()
        self.dealers_card[self.dealer] = [self.game.get_dealt_card(), self.game.get_dealt_card_value()]

    def second_card(self) -> None:
        for player in self.game.get_players():
            self.game.deal_card()
            self._extracted_hit(player)
        self.game.deal_card()
        self.dealers_card[self.dealer][0] += self.game.get_dealt_card()
        self.dealers_card[self.dealer][-1] += self.game.get_dealt_card_value()
    
    def _extracted_hit(self, player: str) -> None:
            self.players_first_two_cards[player][0] += self.game.get_dealt_card()
            self.players_first_two_cards[player][-1] += self.game.get_dealt_card_value()
    
    def players_hit(self) -> None:
        for player in self.players_first_two_cards:
            while self.valid.get_valid_string(f'Do you want to hit {player}? Enter yes, or no! ', 'yes', 'no') == 'yes':
                self.game.deal_card()
                self._extracted_hit(player)
                if self.players_first_two_cards[player][-1] > 21:
                    print(f'{player}, you lost! ')
                    break
                print(self.players_first_two_cards)
                continue
            
    def dealer_hit(self) -> None:
        while self.dealers_card[self.dealer][-1] < 16:
            self.game.deal_card()
            if self.dealers_card[self.dealer][-1] > 21: return
            self.dealers_card[self.dealer][0] += self.game.get_dealt_card()
            self.dealers_card[self.dealer][-1] += self.game.get_dealt_card_value()
    
    def view_players_hand(self) -> None:
        for card, value in self.players_first_two_cards.items(): print(card,'->',value)
    
    def view_dealer_hand(self) -> None:
        for card, value in self.dealers_card.items(): print(card,'->',value)
            
    def split(self): pass
    def double(self): pass