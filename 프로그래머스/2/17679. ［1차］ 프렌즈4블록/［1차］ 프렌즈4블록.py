M,N=0,0
flagMap=[]
def remakeBoard(boards):
    for x in range(N):
        for y in range(0,M):
            for z in range(y,0,-1):
                if boards[z][x]=='0':
                    boards[z][x]=boards[z-1][x]
                    boards[z-1][x]='0'
                    

            
def findAndRemove(boards):
    cnt=0
    global flagMap
    flagMap=[[1 for _ in range(N)] for _ in range(M)]
    for y in range(M-1):
        for x in range(N-1):
            if boards[y][x]=='0':
                continue
            block=boards[y][x]
            if boards[y+1][x]==block and boards[y][x+1]==block and boards[y+1][x+1]==block:
                if flagMap[y][x]==1: flagMap[y][x]=0; cnt+=1
                if flagMap[y][x+1]==1: flagMap[y][x+1]=0; cnt+=1
                if flagMap[y+1][x]==1: flagMap[y+1][x]=0; cnt+=1
                if flagMap[y+1][x+1]==1: flagMap[y+1][x+1]=0; cnt+=1

    for y in range(M):
        for x in range(N):
            if flagMap[y][x]==0:
                boards[y][x]='0'
    return cnt
            

def solution(m, n, board):
    boards=[list(i) for i in board ]
    global M,N
    answer=0
    M,N=m,n
    flagMap=[[1 for _ in range(n)] for _ in range(m)]

    while True:
        addScore=findAndRemove(boards)
        if addScore==0:
            break
        answer+=addScore
        remakeBoard(boards)
    
    remakeBoard(boards)
    return answer