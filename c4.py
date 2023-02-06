import os

col1 = [" ", " ", " ", " ", " ", " "]
col2 = [" ", " ", " ", " ", " ", " "]
col3 = [" ", " ", " ", " ", " ", " "]
col4 = [" ", " ", " ", " ", " ", " "]
col5 = [" ", " ", " ", " ", " ", " "]
col6 = [" ", " ", " ", " ", " ", " "]
col7 = [" ", " ", " ", " ", " ", " "]
red = "\u001b[31m"
blue = "\u001b[34m"
white = "\u001b[37m"
board = [col1, col2, col3, col4, col5, col6, col7]
turn = 0
player = 'nothing'

def print_board():
    global board
    print("  1    2    3    4    5    6    7")
    for i in range(0,35):
        print("-", end='')
    print()
    for y in range(-1,-7,-1):
        for x in range(0,7):
            print("|",board[x][y], "|", end='')
            if x == 6:
                print()
                for z in range(0,35):
                    print("-", end='')
                print()

def place():
    global board
    for i in range(0,6):
        if " " in board[player_input]:
            if board[player_input][i] == " ":
                if turn % 2 == 0:
                    board[player_input][i] = (red + "O" + white)
                    break
                elif turn % 2 != 0:
                    board[player_input][i] = (blue + "O" + white)
                    break
        else:
            print("you can't place something here, try again")
            continue

for t in range(0,42):
    if turn % 2 == 0:
        player = "X"
    else:
        player = "O"

    os.system('clear')
    print_board()
    print()
    player_input = int(input("Choose your column %s:" % player)) - 1
    place()
    turn = turn + 1