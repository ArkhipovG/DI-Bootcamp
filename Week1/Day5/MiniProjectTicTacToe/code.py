board = [' ' for _ in range(9)]
player = 'X'
columns = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]


def end():
    print("End of the game!")
    if check_win(board) and player == "X":
        print(f"The winner is {player}")
    elif check_win(board) and player == "O":
        print(f"The winner is {player}")
    else:
        print("The game ends in a tie.")


def display_board():
    print("TIC TAC TOE")
    print("*****************")
    print('*   ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + "   *")
    print('*  -----------  *')
    print('*   ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + "   *")
    print('*  -----------  *')
    print('*   ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + "   *")
    print("*****************")
    print(" ")


def player_input(player):
    print(f"Player {player}'s turn...")
    user_row = int(input("Enter row: "))
    user_column = int(input("Enter column: "))

    if player == 'X':
        board[(columns[user_column - 1][user_row - 1])] = "X"
    elif player == 'O':
        board[(columns[user_column - 1][user_row - 1])] = "O"
    else:
        print("Invalid input")

    print(" ")


def check_win(board):
    if board[0] == board[1] == board[2] != " ":
        return True
    if board[0] == board[3] == board[6] != " ":
        return True
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[1] == board[4] == board[7] != " ":
        return True
    if board[2] == board[5] == board[8] != " ":
        return True
    if board[3] == board[4] == board[5] != " ":
        return True
    if board[6] == board[7] == board[8] != " ":
        return True
    if board[2] == board[4] == board[8] != " ":
        return True
    else:
        return False


def check_full_board(board):
    filled_cells = 0
    for i in range(0, 9):
        if board[i] != ' ':
            filled_cells += 1

    if filled_cells == 9:
        return True


def change_player(player):
    if player == "X":
        return "O"
    elif player == "O":
        return "X"


def play():
    print("Welcome to Tic-Tac-Toe!")
    player = 'X'
    is_finished = False

    while not is_finished:
        display_board()
        player_input(player)
        player = change_player(player)
        if check_win(board) or check_full_board(board):
            is_finished = True

    display_board()
    end()



play()
