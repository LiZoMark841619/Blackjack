from blackjack import Game
from base_klasses import Valid

def _extracted_from_main_5(game) -> None:
    game.view_player_hand()
    game.view_dealer_hand()

def main():
    blackjack_test = Game()
    valid = Valid()
    bets = blackjack_test.game.get_players_bets()
    print(f'You can see your bets as follows:\n{bets}')
    print('\nFirst card of the players and the dealer!\n')
    blackjack_test.first_card()
    _extracted_from_main_5(blackjack_test)
    for player in blackjack_test.game.get_players():
        if blackjack_test.dealers_card[blackjack_test.dealer][0][0] == 'A':
            insurance_yes_or_no = valid.get_valid_string('Would you like to get insurance? Enter yes or no! ', 'yes', 'no')
            if insurance_yes_or_no == 'yes':
                blackjack_test.get_insurance(player, blackjack_test.game.get_players_bets()[player]//2)
    print('\nFirst 2 cards of the players and the dealer!\n')
    blackjack_test.second_card()
    _extracted_from_main_5(blackjack_test)
    for player in blackjack_test.game.get_players():
        surrendering = valid.get_valid_string(f'Would you like to surrender your cards {player}? Enter yes or no! ', 'yes', 'no')
        if surrendering == 'yes': blackjack_test.surrendering(player)
        else: blackjack_test.player_hit(player)
    blackjack_test.dealer_hit()
    _extracted_from_main_5(blackjack_test)
    print(f'Here are your winnings:\n{blackjack_test.game.get_players_bets()}')
    
if __name__ == '__main__': main()