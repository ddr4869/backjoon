import sys
input = sys.stdin.readline

n, l = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def solve(k, direction):
    if direction == 0:
        line = maps[k]
    else:  
        line = [maps[i][k] for i in range(n)]
    
    disable = [False] * n  
    i = 0
    
    while i < n - 1:
        if line[i] == line[i + 1]:
            i += 1
            continue
        elif line[i] + 1 == line[i + 1]:  
            for j in range(l):
                if i - j < 0 or line[i] != line[i - j] or disable[i - j]:
                    return False
            for j in range(l):
                disable[i - j] = True
        elif line[i] - 1 == line[i + 1]:  
            for j in range(1, l + 1):
                if i + j >= n or line[i + 1] != line[i + j] or disable[i + j]:
                    return False
            for j in range(1, l + 1):
                disable[i + j] = True
            i += l - 1 
        else: 
            return False
        i += 1
    return True

for i in range(n):
    if solve(i, 0): 
        answer += 1
    if solve(i, 1): 
        answer += 1

print(answer)
