import sys
input = sys.stdin.readline

n, t = map(int, input().split())
boards=[[]]
dp=[[0 for j in range(n+1)] for i in range(n+1)]
initList=[0]
for i in range(1,n+1):
    board=initList+list(map(int, input().split()))
    boards.append(board)
dp[1][1]=boards[1][1]

for x in range(1,n+1):
    for y in range(1,n+1):
        dp[x][y]=boards[x][y]+dp[x-1][y]+dp[x][y-1]-dp[x-1][y-1]

for _ in range(t):
    x1,y1,x2,y2=map(int, input().split())
    print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])
