import sys
input = sys.stdin.readline

n = int(input())
boards=[]
dp=[[0 for j in range(n)] for i in range(n)]

for i in range(n):
    board=list(map(int, input().split()))
    boards.append(board)

def solve(y, x):
    if y==n-1 and x==n-1:
        return 1
    if y>=n or x>=n or (boards[y][x]==0):
        return 0
    if dp[y][x]>0:
        return dp[y][x]
    jump=boards[y][x]
    dp[y][x]=solve(y+jump,x)+solve(y,x+jump)
    return dp[y][x]

solve(0,0)
print(dp[0][0])