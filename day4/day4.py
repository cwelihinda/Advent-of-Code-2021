import re
def construct_game_sim(lines):
    draws = lines[0].split(",")
    boards = []
    board = []
    for index, line in enumerate(lines, 2):
        if(line == ""):
            boards.append(board)
            board = []
        else:
            row = re.split("\s+", line.strip())
            board.append([row, [False] * len(row)])
    boards.append(board)
    return draws, boards

def check_board(board, row, col):
    #check the row
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


def play_bingo(boards, draws):
    for draw in draws:
        winner = None
        for board in boards:
            winner = play_board(board, draw)
            if(winner is not None):
                return winner, draw
        
def get_game_score(winner):
    total = 0
    for i in range(len(winner[0][1])):
        for j in range(len(winner)):
            if(not winner[i][1][j]):
                total += int(winner[i][0][j])
    return total
lines = open("day4_in.txt", "r").read().split("\n")
draws, boards = construct_game_sim(lines)

winner, draw = play_bingo(boards, draws)

print(winner)
print(draw)
print(get_game_score(winner))
print(get_game_score(winner) * int(draw))

