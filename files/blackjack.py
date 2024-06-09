from base_klasses import Valid, Bet, Player, Dealer, FrenchDeck
from typing import Any
import random

class Blackjack(Valid):
    def __init__(self) -> None:
        self._cards = FrenchDeck()
        self._dealers = Dealer()
        chosen_dealer = self.get_valid_number(f'Choose your dealer from {self._dealers.get_options}! ', 0, list(self._dealers.get_options.keys())[-1])
        num_players = self.get_valid_number('Enter the number of players from 1 to 4! ', 1, 4)
        players = [Player() for _ in range(num_players)]
        self.__dealer = self._dealers.get_options[chosen_dealer]
        self.__players = [player.get_player_name for player in players]

    def get_dealer(self) -> str:
        return f'Dealer: {self.__dealer}'
            
    def get_players(self) -> list:
        return self.__players
        
    def welcome(self) -> None:
        print(f'Welcome to game {self.__class__.__name__} {self.get_players()}! ')

    def deal_card(self) -> None:
        card = random.choice(self._cards._deck)
        self._cards._deck.remove(card)
        return card
    
    def get_dealt_card_value(self, card) -> int:
        return self._cards._values[card]

class Game:
    def __init__(self) -> None:
        self.game = Blackjack()
        self.game.welcome()
        self.dealer = self.game.get_dealer()
        self.players_first_two_cards: dict[str, list] = {}
        self.dealers_card: dict[Any, Any] = {}
        bets = [Bet() for _ in range(len(self.game.get_players()))]
        self.bets = [bet.make_your_bet() for bet in bets]
    
    def first_card(self) -> None:
        for player in self.game.get_players():
            card = self.game.deal_card()
            self.players_first_two_cards[player] = [card, self.game.get_dealt_card_value(card)]
        card = self.game.deal_card()
        self.dealers_card[self.dealer] = [card, self.game.get_dealt_card_value(card)]

    def second_card(self) -> None:
        for player in self.game.get_players():
            card = self.game.deal_card()
            self._extracted_hit_player(player, card)
        card = self.game.deal_card()
        self._extracted_hit_dealer(card)
    
    def _extracted_hit_player(self, player: str, card) -> None:
        self.players_first_two_cards[player][0] += card
        self.players_first_two_cards[player][-1] += self.game.get_dealt_card_value(card)
        if self.players_first_two_cards[player][-1] < 10 and card == 'A': self.players_first_two_cards[player][-1] += 10
            
    def _extracted_hit_dealer(self, card) -> None:
        self.dealers_card[self.dealer][0] += card
        self.dealers_card[self.dealer][-1] += self.game.get_dealt_card_value(card)
        if self.dealers_card[self.dealer][-1] < 10 and card == 'A': self.dealers_card[self.dealer][-1] += 10
        
    def player_hit(self) -> None:
        for player in self.players_first_two_cards:
            while self.game.get_valid_string(f'\nDo you want to hit {player}? Enter yes, or no! ', 'yes', 'no') == 'yes':
                card = self.game.deal_card()
                self._extracted_hit_player(player, card)
                if self.players_first_two_cards[player][-1] > 21: print(f'{player}, you lost! '); break
                print(self.players_first_two_cards); continue
            
    def dealer_hit(self) -> None:
        while self.dealers_card[self.dealer][-1] < 16:
            card = self.game.deal_card()
            if self.dealers_card[self.dealer][-1] > 21: return
            self._extracted_hit_dealer(card)
    
    def view_player_hand(self) -> None:
        for player, card_and_value in self.players_first_two_cards.items(): print(player,'->',card_and_value)
    
    def view_dealer_hand(self) -> None:
        for dealer, card_and_value in self.dealers_card.items(): print(dealer,'->',card_and_value)
            
    def split(self): pass
    def double(self): pass