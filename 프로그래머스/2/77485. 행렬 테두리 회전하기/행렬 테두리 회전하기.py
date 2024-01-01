def rotate(query, board):
    x1,y1,x2,y2=query[0],query[1],query[2],query[3]
    lefttop=board[x1][y1]
    leftdown=board[x2][y1]
    righttop=board[x1][y2]
    rightdown=board[x2][y2]
    ans=lefttop
    
    for i in range(x1,x2+1):
        ans=min(ans, board[i][y1])
        ans=min(ans, board[i][y2])
    for i in range(y1,y2+1):
        ans=min(ans, board[x1][i])
        ans=min(ans, board[x2][i])
        
    for i in range(y2,y1,-1):
        board[x1][i]=board[x1][i-1]
        ans=min(ans, board[x1][i])
    for j in range(x2,x1,-1):
        board[j][y2]=board[j-1][y2]
        ans=min(ans, board[j][y2])
    for k in range(y1,y2):
        board[x2][k]=board[x2][k+1]
        ans=min(ans, board[x2][k])
    for l in range(x1,x2):
        board[l][y1]=board[l+1][y1]
        ans=min(ans, board[l][y1])
        

        
    board[x1][y1+1]=lefttop
    board[x1+1][y2]=righttop
    board[x2][y2-1]=rightdown
    board[x2-1][y1]=leftdown
    return board, ans
    
    

def solution(rows, columns, queries):
    answer = []
    cnt=1
    board=[[0 for _ in range(columns)] for _ in range(rows)]

    for x in range(rows):
        for y in range(columns):
            board[x][y]=cnt
            cnt+=1
    
    for query in queries:
        for i,v in enumerate(query):
            query[i]-=1
        board,ans=rotate(query, board)
        answer.append(ans)
        # for i in board:
        #     print(i)
        # print()

    return answer