from itertools import product

class Valid:
    def get_valid_number(self, prompt: str, min_val: int, max_val:int) -> int:
        while True:
            try:
                value = int(input(prompt))
                if value in range(min_val, max_val+1):
                    return value
                print('Invalid number! Please try again! ')
            except ValueError:
                print('Invalid value! Please enter a valid number! ')
    
    def get_valid_string(self, prompt: str, *args) -> str:
        while True:
            value = input(prompt)
            if value in args:
                return value
            print('Invalid value, try again! ')

class Bet:
    def __init__(self) -> None:
        self.valid = Valid()
        self.__bet = self.valid.get_valid_number('Make your bets from 5 to 100 dollars! ', 5, 100)
        
    def make_bet(self) -> int:
        return self.__bet

class Dealer:
    def __init__(self) -> None:
        self.__options = {0:'John', 1:'Kate', 2:'Robert', 3:'Elizabeth'}
        
    @property
    def get_options(self) -> dict:
        return self.__options
    
class Player:
    number_of_instances = 0
    
    def __init__(self) -> None:
        Player.number_of_instances += 1
        self.__name = input(f'Enter the #{Player.number_of_instances} Player name! ')
        
    @property
    def get_name(self) -> str:
        return self.__name.title()
    
class FrenchDeck:
    def __init__(self) -> None:
        self._cards = list(range(2, 11)) + list('JQKA')
        self._deck = list(product(self._cards, 'SHDC'))
        self._values = {card:card[0] if isinstance(card[0], int) else 1 if card[0] == 'A' else 10 for card in self._deck}