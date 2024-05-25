import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

time = 0

def is_finish(board):
    for row in board:
        if 1 in row:
            return False
    return True

def mark_inner_empty_spaces(board, inners):
    visited = [[False] * m for _ in range(n)]
    queue = deque([(0, 0)])
    visited[0][0] = True
    inners[0][0] = 0

    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                if board[ny][nx] == 0:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    inners[ny][nx] = 0

while True:
    if is_finish(board):
        print(time)
        break

    time += 1
    inners = [[1] * m for _ in range(n)]
    mark_inner_empty_spaces(board, inners)
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
    melting = []

    for y in range(n):
        for x in range(m):
            if board[y][x] == 1:
                cnt = 0
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if 0 <= ny < n and 0 <= nx < m and inners[ny][nx] == 0:
                        cnt += 1
                if cnt >= 2:
                    melting.append((y, x))

    for y, x in melting:
        board[y][x] = 0