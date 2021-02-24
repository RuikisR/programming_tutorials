
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

# So this is absolutely terrible, don't do this

# Fixing it up:

'''
1: Global Constants
PLAYERS = ['O', 'X']
EMPTY = '#'

2: Function for game initialisation

def create_game(game_size=3):
    return [[EMPTY for _ in range(game_size)] for _ in range(game_size)]

3: Function for displaying game

def display_game(game):
    print("\n".join([" ".join([item for item in row]) for row in game]))

4: Player management

player_number = 0

def next_player(current_player_number):
    return (current_player_number + 1) % len(PLAYERS)

5: Make a move

def make_move(game, player_number, row, col):
    if row < 0 or row >= len(game):
        return False
    if col < 0 or col >= len(game):
        return False
    game[row][col] = PLAYERS[player_number]
    return True

6: Checking for winners

def check_row_winners(game):
    for row in game:
        if row[0] != EMPTY and row.count(row[0]) == len(row):
            return row[0]
    return None

def check_col_winners(game):
    for col in range(len(game)):
        checking_col = [row[col] for row in game]
        if checking_col[0] != EMPTY and checking_col.count(checking_col[0]) == len(checking_col):
            return checking_col[0]
    return None

def check_left_diag_winners(game):
    if game[0][0] != EMPTY:
        for check in range(len(game) - 1):
            if game[check][check] != game[check + 1][check + 1]:
                return None
        return game[0][0]
    return None

def check_right_diag_winners(game):
    if game[0][-1] != EMPTY:
        for check in range(len(game) - 1):
            col = len(game) - check - 1
            if game[check][col] != game[check + 1][col - 1]:
                return None
        return game[0][-1]
    return None


def check_winners(game):
    winner = check_row_winners(game)
    if winner is not None:
        return winner
    winner = check_col_winners(game)
    if winner is not None:
        return winner
    winner = check_left_diag_winners(game)
    if winner is not None:
        return winner
    winner = check_right_diag_winners(game)
    return winner

7: Putting it all together

PLAYERS = ['O', 'X']
EMPTY = '#'


def create_game(game_size=3):
    return [[EMPTY for _ in range(game_size)] for _ in range(game_size)]


def display_game(game):
    print("\n".join([" ".join([item for item in row]) for row in game]))


def next_player(current_player_number):
    return (current_player_number + 1) % len(PLAYERS)


def make_move(game, player_number, row, col):
    if row < 0 or row >= len(game):
        return False
    if col < 0 or col >= len(game):
        return False
    game[row][col] = PLAYERS[player_number]
    return True

def check_row_winners(game):
    for row in game:
        if row[0] != EMPTY and row.count(row[0]) == len(row):
            return row[0]
    return None

def check_col_winners(game):
    for col in range(len(game)):
        checking_col = [row[col] for row in game]
        if checking_col[0] != EMPTY and checking_col.count(checking_col[0]) == len(checking_col):
            return checking_col[0]
    return None

def check_left_diag_winners(game):
    if game[0][0] != EMPTY:
        for check in range(len(game) - 1):
            if game[check][check] != game[check + 1][check + 1]:
                return None
        return game[0][0]
    return None

def check_right_diag_winners(game):
    if game[0][-1] != EMPTY:
        for check in range(len(game) - 1):
            col = len(game) - check - 1
            if game[check][col] != game[check + 1][col - 1]:
                return None
        return game[0][-1]
    return None


def check_winners(game):
    winner = check_row_winners(game)
    if winner is not None:
        return winner
    winner = check_col_winners(game)
    if winner is not None:
        return winner
    winner = check_left_diag_winners(game)
    if winner is not None:
        return winner
    winner = check_right_diag_winners(game)
    return winner


def main():
    print("Welcome to Tic-Tac-Toe!")
    playing = True
    player = 0
    game = create_game()

    while playing:
        display_game(game)
        playing = False
        # TODO: Finish this little wrap up
