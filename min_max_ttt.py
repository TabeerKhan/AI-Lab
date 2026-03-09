import math

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board():
    for row in board:
        print("|".join(row))
        print("-"*5)

def check_winner(player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_full():
    for row in board:
        if ' ' in row:
            return False
    return True

def minimax(depth, is_max):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_full():
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(depth+1, False)
                    board[i][j] = ' '
                    best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(depth+1, True)
                    board[i][j] = ' '
                    best = min(best, score)
        return best

def best_move():
    best_score = -math.inf
    move = (0,0)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(0, False)
                board[i][j] = ' '

                if score > best_score:
                    best_score = score
                    move = (i,j)

    board[move[0]][move[1]] = 'O'

while True:

    print_board()

    r = int(input("Enter row (0-2): "))
    c = int(input("Enter column (0-2): "))

    if board[r][c] == ' ':
        board[r][c] = 'X'
    else:
        print("Invalid Move")
        continue

    if check_winner('X'):
        print_board()
        print("Human Wins")
        break

    if is_full():
        print_board()
        print("Draw")
        break

    best_move()

    if check_winner('O'):
        print_board()
        print("AI Wins")
        break

    if is_full():
        print_board()
        print("Draw")
        break