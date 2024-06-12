import sys
input = sys.stdin.readline
str1 = [' ']+list(input().strip())
str2 = [' ']+list(input().strip())
str3 = [' ']+list(input().strip())
str1_len = len(str1)
str2_len = len(str2)
str3_len = len(str3)
dp = [[[0 for _ in range(str3_len)] for _ in range(str2_len)] for _ in range(str1_len)]
for i in range(str1_len):
    for j in range(str2_len):
        for k in range(str3_len):
            if i==0 or j==0 or k==0:
                dp[i][j][k] = 0
            else:
                if str1[i] == str2[j] == str3[k]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
print(dp[-1][-1][-1])