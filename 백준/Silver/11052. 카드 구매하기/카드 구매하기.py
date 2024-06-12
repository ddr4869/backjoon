import sys
n = int(input())
cards = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
dp[1] = cards[1]
def solve(k):
    if dp[k]: 
        return dp[k]
    max_value = cards[k]
    for i in range(1, k):
        cost = cards[i] + solve(k-i)
        if cost > max_value:
            max_value = cost
    dp[k] = max_value
    return max_value

print(solve(n))