import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

def check_answer(board):
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    visited = [[False for _ in range(m)] for _ in range(n)]
    iceberg_count = 0

    for i in range(1, n-1):
        for j in range(1, m-1):
            if board[i][j] != 0 and not visited[i][j]:
                iceberg_count += 1
                if iceberg_count > 1:
                    return True  # 분리된 빙산이 2개 이상 있음
                dq = deque()
                dq.append((i, j))
                visited[i][j] = True

                while dq:
                    y, x = dq.popleft()
                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]
                        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] != 0 and not visited[ny][nx]:
                            dq.append((ny, nx))
                            visited[ny][nx] = True

    return False  # 분리된 빙산이 1개 이하임

amount = sum(board[i][j] != 0 for i in range(1, n-1) for j in range(1, m-1))

if check_answer(board):
    print(0)
else:
    ans = 0
    while True:
        ans += 1
        be_water = [[0 for _ in range(m)] for _ in range(n)]
        iceberg = 0

        for i in range(1, n-1):
            for j in range(1, m-1):
                if board[i][j] != 0:
                    cnt = 0
                    iceberg += 1
                    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + dy, j + dx
                        if board[ni][nj] == 0:
                            cnt += 1
                    be_water[i][j] = cnt

        if iceberg == 0:
            print(0)
            break

        amount = 0
        for i in range(1, n-1):
            for j in range(1, m-1):
                if board[i][j] != 0:
                    if be_water[i][j] >= board[i][j]:
                        board[i][j] = 0
                    else:
                        board[i][j] -= be_water[i][j]
                        amount += 1

        if check_answer(board):
            print(ans)
            break
