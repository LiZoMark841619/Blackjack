from process import Process

if __name__ == '__main__':
    process = Process()
    process.game()
    print(f'Here are your original bets:\n{process.blackjack.game.get_bets()}')
    process.first_round()
    process.view_hands()
    process.second_round()
    process.view_hands()
    process.result()
    print(f'Here are your winnings:\n{process.blackjack.game.get_bets()}')

    