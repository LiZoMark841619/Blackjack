from blackjack import Game

blackjack = Game()

def view_hands(game) -> None:
    game.view_player_hand()
    game.view_dealer_hand()

def game():
    bets = blackjack.game.get_players_bets()
    print(f'You can see your bets as follows:\n{bets}')
    print('\nFirst card of the players and the dealer!\n')
    
def first_round():
        blackjack.first_card()
        for player in blackjack.game.get_players():
            if blackjack.dealers_card[blackjack.dealer][0][0] == 'A':
                insurance_yes_or_no = blackjack.game.get_valid_string('Would you like to get insurance? Enter yes or no! ', 'yes', 'no')
                if insurance_yes_or_no == 'yes':
                    blackjack.get_insurance(player, blackjack.game.get_players_bets()[player]//2)
def second_round():
    print('\nFirst 2 cards of the players and the dealer!\n')
    blackjack.second_card()
    view_hands(blackjack)
    for player in blackjack.game.get_players():
        surrendering = blackjack.game.get_valid_string(f'Would you like to surrender your cards {player}? Enter yes or no! ', 'yes', 'no')
        if surrendering == 'yes': blackjack.surrendering(player)
        else: blackjack.player_hit(player)
    blackjack.dealer_hit()
    
if __name__ == '__main__':
    game()
    first_round()
    view_hands(blackjack)
    second_round()
    view_hands(blackjack)
    print(f'Here are your winnings:\n{blackjack.game.get_players_bets()}')