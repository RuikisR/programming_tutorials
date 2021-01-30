
print("Welcome to Tic-Tac-Toe!")
playing = True
player = 'O'
game = [['#', '#', '#'],
        ['#', '#', '#'],
        ['#', '#', '#']]

while playing:
    for row in game:
        display = ""
        for item in row:
            display += item + " "
        print(display)
    print(f"Player {player}'s move!")

    player_choice = input("Please input a row number, or quit to exit ")
    if player_choice == "quit":
        playing = False
    else:
        chosen_row = int(player_choice) - 1
        chosen_col = int(input("Please input a column number ")) - 1
        game[chosen_row][chosen_col] = player

        for row in game:
            if player == row[0] == row[1] == row[2]:
                print(f"Congratulations, player {player} wins!")
                playing = False
        for col in range(3):
            if player == game[0][col] == game[1][col] == game[2][col]:
                print(f"Congratulations, player {player} wins!")
                playing = False
        if player == game[0][0] == game[1][1] == game[2][2]:
            print(f"Congratulations, player {player} wins!")
            playing = False
        if player == game[2][0] == game[1][1] == game[0][2]:
            print(f"Congratulations, player {player} wins!")
            playing = False

        if player == 'O':
            player = 'X'
        elif player == 'X':
            player = 'O'
