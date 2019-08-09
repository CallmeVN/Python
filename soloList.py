players = ['Tony', 'Lei', 'Luo', 'Jimmy', 'John', 'Adam', 'Black']
for player1 in players:
    for player2 in players:
        if (player1 == 'Adam' and player2 == 'Lei') or (player2 == 'Adam' and player1 == 'Lei') or (player1 == player2):
            continue
        else:
            print(player1, '  VS  ', player2)