import random

def display_board(board):
    x = "          |          |          "
    line_1 = f"   {board[7]}      |     {board[8]}    |    {board[9]}      "
    z = "__________|__________|__________"
    line_2 = f"   {board[4]}      |     {board[5]}    |    {board[6]}      "
    line_3 = f"   {board[1]}      |     {board[2]}    |    {board[3]}      "
    print(x)
    print(line_1)
    print(z)
    print(x)
    print(line_2)
    print(z)
    print(x)
    print(line_3)
    print(x)

def position_guide():
    x = "         |          |          "
    y1= "   7     |     8    |    9      "
    z = "_________|__________|__________"
    y2= "   4     |     5    |   6      "
    y3= "   1     |     2    |    3      "
    print(x)
    print(y1)
    print(z)
    print(x)
    print(y2)
    print(z)
    print(x)
    print(y3)
    print(x)


def player_input():
    marker = ''
    while marker not in {'X', 'O'}:
        marker = input('Player_1 : Choose (X/O): ').upper

    return ('X', 'O') if marker == 'X' else ('O', 'X')

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board, mark):
    if (board[7] == mark and board[8] == mark and board[9] == mark):
        return True

    elif (board[4] == mark and board[5] == mark and board[6] == mark):
        return True

    elif (board[1] == mark and board[2] == mark and board[3] == mark):
        return True

    elif (board[7] == mark and board[4] == mark and board[1] == mark):
        return True

    elif (board[8] == mark and board[5] == mark and board[2] == mark):
        return True

    elif (board[9] == mark and board[6] == mark and board[3] == mark):
        return True

    elif (board[7] == mark and board[5] == mark and board[3] == mark):
        return True

    elif (board[9] == mark and board[5] == mark and board[1] == mark):
        return True

    else:
        return False


def choose_first():
    return 'Player_2' if random.randint(0,1) == 0 else 'Player_1'

def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    return not any(space_check(board,i) for i in range(1, 10))

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose your next position (1-9): '))

    return position

def replay():
    return input("Do you want to play again?? (y/n): ").lower().startswith('y')


if __name__ == "__main__":
    print("Welcome to Tic-Tac-toe Game !")
    while True:
        theBoard = [' '] * 10
        Player_1_marker = input("Player_1, please select your mark(x/o or whatever): ")
        Player_2_marker = input("Player_2, please select your mark(x/o or whatever): ")
        turn = choose_first()
        print(f'{turn} will go first.')
        play_game = input('Are you ready to play the game?? (y/n): ')
        game_on = play_game.lower() == 'y'
        while game_on:
            if turn == 'Player_1':
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard,Player_1_marker,position)

                if win_check(theBoard,Player_1_marker):
                    display_board(theBoard)
                    print('Congratulations! Player_1 have won the game!')
                    game_on = False

                elif full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is Draw..')
                    break
                else:
                    turn = 'Player_2'

            else:
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard,Player_2_marker,position)

                if win_check(theBoard,Player_2_marker):
                    display_board(theBoard)
                    print('Congratulations! Player_2 have won the game!')
                    game_on = False

                elif full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is Draw..')
                    break
                else:
                    turn = 'Player_1'

        if not replay():
            break
