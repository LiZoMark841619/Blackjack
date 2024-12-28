from process import Process
# import shelve

if __name__ == '__main__':
    process = Process()
    process.display_bets()
    print('\nFirst card of the players and the dealer!\n')
    players = process.blackjack.game.get_players()
    process.get_one_round(process.blackjack.deal_cards, players)
    process.view_hands()
    process.insurance_against_blackjack(players)
    print('\nFirst 2 cards of the players and the dealer!\n')
    process.get_one_round(process.blackjack.deal_cards, players)
    process.view_hands()
    process.surrender(players)
    process.view_hands()
    print(f'Here are your winnings:\n{process.check_winnings()}')
    # db = shelve.open('winning_results')
    # for name in process.check_winnings():
    #     db[name] = process.check_winnings()[name]
    # db.close()
    # db = shelve.open('winning_results')
    # for key in db:
    #     print(key, '->', db[key])