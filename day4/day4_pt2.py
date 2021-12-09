import re
def construct_game_sim(lines):
    draws = lines[0].split(",")
    boards = []
    board = []
    for index, line in enumerate(lines):
        if(line == ""):
            boards.append(board)
            board = []
        else:
            row = re.split("\s+", line.strip())
            board.append([row, [False] * len(row)])
    boards.append(board)
    return draws, boards

def check_board(board, row, col):
    winner = True
    for i in range(len(board[0][1])):
        winner = winner and board[row][1][i]
    if(winner):
        return True
    winner = True
    for i in range(len(board)):
        winner = winner and board[i][1][col]
    return winner

def play_board(board, draw):
    for i in range(len(board[0][1])):
        for j in range(len(board)):
            if(board[i][0][j] == draw):
                board[i][1][j] = True
                if(check_board(board, i, j)):
                    return board
    return None

def do_bingo(boards, draw):
    losers = []
    for board in boards:
        winner = None
        winner = play_board(board, draw)
        if(winner is not None and len(boards) == 1):
            return [winner], True
        elif(winner is None):
            losers.append(board)
    return losers, False

def play_bingo(boards, draws):
    for draw in draws:
        boards, done = do_bingo(boards, draw)
        if(len(boards) == 1 and done):
            return boards[0], draw
        
def get_game_score(winner):
    total = 0
    for i in range(len(winner[0][1])):
        for j in range(len(winner)):
            if(not winner[i][1][j]):
                total += int(winner[i][0][j])
    return total
lines = open("day4_in.txt", "r").read().split("\n")
draws, boards = construct_game_sim(lines)
winner, draw = play_bingo(boards[1:], draws)

print(get_game_score(winner) * int(draw))

