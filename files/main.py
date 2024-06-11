from process import Process

if __name__ == '__main__':
    process = Process()
    process.game()
    process.first_round()
    process.view_hands()
    process.second_round()
    process.view_hands()
    print(f'Here are your winnings:\n{process.blackjack.game.get_bets()}')