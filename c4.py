import os
import time

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
player = ''
winnerX = False
winnerO = False

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
        if board[player_input][i] == " ":
            if turn % 2 == 0:
                board[player_input][i] = (red + "O" + white)
                break
            elif turn % 2 != 0:
                board[player_input][i] = (blue + "O" + white)
                break

def IswinnerDiagUp():
    global board
    global winnerO
    global winnerX
    for x in range(0,4):
        for y in range(0,3):
            if board[x][y] == (red + "O" + white):
                if board[x+1][y+1] == (red + "O" + white):
                    if board[x+2][y+2] == (red + "O" + white):
                        if board[x+3][y+3] == (red + "O" + white):
                            winnerX = True
            elif board[x][y] == (blue + "O" + white):
                if board[x+1][y+1] == (blue + "O" + white):
                    if board[x+2][y+2] == (blue + "O" + white):
                        if board[x+3][y+3] == (blue + "O" + white):
                            winnerO = True

def IswinnerDiagDown():
    global board
    global winnerO
    global winnerX
    for x in range(0,4):
        for y in range(3,6):
            if board[x][y] == (red + "O" + white):
                if board[x+1][y-1] == (red + "O" + white):
                    if board[x+2][y-2] == (red + "O" + white):
                        if board[x+3][y-3] == (red + "O" + white):
                            winnerX = True
            elif board[x][y] == (blue + "O" + white):
                if board[x+1][y-1] == (blue + "O" + white):
                    if board[x+2][y-2] == (blue + "O" + white):
                        if board[x+3][y-3] == (blue + "O" + white):
                            winnerO = True

def IswinnerRow():
    global board
    global winnerX
    global winnerO
    for y in range(0,6):
        for x in range(0,4):
            if board[x][y] == (red + "O" + white):
                if board[x+1][y] == (red + "O" + white):
                    if board[x+2][y] == (red + "O" + white):
                        if board[x+3][y] == (red + "O" + white):
                            winnerX = True
            elif board[x][y] == (blue + "O" + white):
                if board[x+1][y] == (blue + "O" + white):
                    if board[x+2][y] == (blue + "O" + white):
                        if board[x+3][y] == (blue + "O" + white):
                            winnerO = True
                

def IswinnerCol():
    global board
    global winnerX
    global winnerO
    for x in range(0,7):
        for y in range(0,3):
            if board[x][y] == (red + "O" + white):
                if board[x][y+1] == (red + "O" + white):
                    if board[x][y+2] == (red + "O" + white):
                        if board[x][y+3] == (red + "O" + white):
                            winnerX = True
            elif board[x][y] == (blue + "O" + white):
                if board[x][y+1] == (blue + "O" + white):
                    if board[x][y+2] == (blue + "O" + white):
                        if board[x][y+3] == (blue + "O" + white):
                            winnerO = True
            else:
                continue

while turn <= 42:
    if turn % 2 == 0:
        player = (red + "O" + white)
    else:
        player = (blue + "O" + white)

    os.system('clear')
    print_board()
    print()
    IswinnerRow()
    IswinnerCol()
    IswinnerDiagUp()
    IswinnerDiagDown()
    if turn == 42:
        print("The Game is a draw")
    else:
        if winnerX == True:
            print("Red won!")
            break
        elif winnerO == True:
            print("Blue won!")
            break
        else:
            try:
                player_input = int(input("Choose your column %s:" % player)) - 1
            except ValueError:
                print("invalid input, please try again")
                time.sleep(2)
                continue
        if player_input in range(0,7):
                if " " in board[player_input]:
                    place()
                    turn += 1
        else:
            print("Invalid number, please try again")
            time.sleep(2)
            continue             

print()
