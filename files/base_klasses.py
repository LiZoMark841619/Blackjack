class Valid:
    def get_valid_number(self, prompt: str, min_val: int, max_val:int) -> int:
        while True:
            try:
                value = int(input(prompt))
                if min_val <= value <= max_val: return value
                print('Invalid number! Please try again! ')
            except ValueError: print('Invalid value! Please enter a valid number! ')
    
    def get_valid_string(self, prompt: str, *args):
        while True:
            value = input(prompt)
            if value in args: return value
            print('Invalid value, try again! ')

class Bet:
    def __init__(self) -> None:
        valid = Valid()
        self.__bet = valid.get_valid_number('Make your bet from 10 to 1000 dollars! ', 10, 1000)
        
    def make_your_bet(self) -> int:
        return self.__bet

class Dealer:
    def __init__(self) -> None:
        self.__options = dict(enumerate(['John', 'Kate', 'Robert', 'Elizabeth']))
    @property
    def get_options(self) -> dict:
        return self.__options
    
class Player:
    def __init__(self) -> None:
        self.__name = input('Enter your name! ').title()
    @property
    def get_player_name(self) -> str:
        return self.__name
    
class FrenchDeck:
    def __init__(self) -> None:
        self._cards = list(range(2, 11)) + list('JQKA')
        self._deck = [(card, color) for card in self._cards for color in 'SHDC']
        self._values = {card:card[0] if type(card[0]) == int else 1 if card[0] == 'A' else 10 for card in self._deck}