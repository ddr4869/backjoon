def check_straight(board, mark):
    for i in range(3):
        if board[i][0]==mark and board[i][1]==mark and board[i][2]==mark: return True
        if board[0][i]==mark and board[1][i]==mark and board[2][i]==mark: return True
    if board[0][0]==mark and board[1][1]==mark and board[2][2]==mark: return True
    if board[2][0]==mark and board[1][1]==mark and board[0][2]==mark: return True
    return False


def solution(board):
    o_cnt,x_cnt=0,0
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x]=='O': o_cnt+=1
            if board[y][x]=='X': x_cnt+=1
    if o_cnt<x_cnt or o_cnt-x_cnt>1: return 0

    if check_straight(board, 'O'):
        if o_cnt==x_cnt: return 0
    if check_straight(board, 'X'):
        if o_cnt>x_cnt: return 0
    return 1