import sys 
sys.setrecursionlimit(10000)

def solution(maps):
    height,width=len(maps),len(maps[0])
    NY,NX=[1,-1,0,0],[0,0,1,-1]
    isvisited=[[0 for _ in range(width)] for _ in range(height)]
    def dfs(y,x):
        isvisited[y][x]=1
        cnt=int(maps[y][x])
        for i in range(4):
            ny,nx=y+NY[i],x+NX[i]
            if 0<=ny<height and 0<=nx<width and not isvisited[ny][nx] and maps[ny][nx]!='X':
                cnt+=dfs(ny,nx)
        return cnt
    
    answer=[]
    for y in range(height):
        for x in range(width):
            if maps[y][x]!='X' and isvisited[y][x]==0:
                answer.append(dfs(y,x))
    answer.sort() 
    return answer if len(answer) else [-1]