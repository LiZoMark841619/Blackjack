from blackjack import Game

def _extracted_from_main_5(game, arg: str = '') -> None:
    game.view_players_hand()
    if arg: print(arg)
    game.view_dealer_hand()

def main():
    game = Game()
    print('\nFirst card of the players!\n')
    game.first_card()
    _extracted_from_main_5(game, '\nFirst card of the dealer!\n')
    print('\nFirst and second card of the players!\n')
    game.second_card()
    _extracted_from_main_5(game, '\nFirst and second card of the dealer!\n')
    game.players_hit()
    game.dealer_hit()
    _extracted_from_main_5(game)
    
if __name__ == '__main__': main()