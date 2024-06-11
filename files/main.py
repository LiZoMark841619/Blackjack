from process import Process

if __name__ == '__main__':
    process = Process()
    process.game()
    print('\nFirst card of the players and the dealer!\n')
    process.first_round()
    process.view_hands()
    print('\nFirst 2 cards of the players and the dealer!\n')
    process.second_round()
    process.view_hands()
    process.result()
    print(f'Here are your winnings:\n{process.blackjack.game.get_bets()}')

    