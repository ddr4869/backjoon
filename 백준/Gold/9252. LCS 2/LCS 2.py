import sys
input = sys.stdin.readline
str1 = [' ']+list(input().strip())
str2 = [' ']+list(input().strip())
str1_len = len(str1)
str2_len = len(str2)
dp = [[0 for _ in range(str2_len)] for _ in range(str1_len)]

for i in range(str1_len):
    for j in range(str2_len):
        if i==0 or j==0:
            dp[i][j] = 0
        else:
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
if dp[-1][-1]:
    answer = []
    y,x = len(str1)-1, len(str2)-1
    while( dp[y][x] ):
        if dp[y][x] == dp[y-1][x]:
            y -= 1
        elif dp[y][x] == dp[y][x-1]:
            x -= 1
        else:
            answer.append(str1[y])
            y -= 1
            x -= 1
    print(''.join(map(str, answer[::-1])))