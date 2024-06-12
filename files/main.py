from process import Process

if __name__ == '__main__':
    process = Process()
    process.display_bets()
    print('\nFirst card of the players and the dealer!\n')
    process.get_one_round(process.blackjack.deal_first_card)
    process.view_hands()
    process.insurance_against_blackjack()
    print('\nFirst 2 cards of the players and the dealer!\n')
    process.get_one_round(process.blackjack.deal_second_card)
    process.view_hands()
    process.surrender()
    process.view_hands()
    print(f'Here are your winnings:\n{process.check_winnings()}')