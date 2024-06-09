from blackjack import Game
from base_klasses import Bet

def _extracted_from_main_5(game) -> None:
    game.view_player_hand()
    game.view_dealer_hand()

def main():
    game = Game()
    print('\nFirst card of the players and the dealer!\n')
    game.first_card()
    _extracted_from_main_5(game)
    print('\nFirst and second card of the players and the dealer!\n')
    game.second_card()
    _extracted_from_main_5(game)
    game.player_hit()
    game.dealer_hit()
    _extracted_from_main_5(game)
    
if __name__ == '__main__': main()