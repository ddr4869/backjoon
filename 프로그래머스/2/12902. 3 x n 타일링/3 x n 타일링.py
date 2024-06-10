def solution(n):
    if n%2!=0: return 0
    dp=[0 for _ in range(n+1)]
    dp[0]=1
    dp[2]=3
    for i in range(4,n+1,2):
        dp[i] += (dp[i-2]*3)
        k = i-4
        while(k>=0):
            dp[i] += (dp[k]*2)
            k -= 2
        dp[i] = dp[i]%1000000007
    return dp[n]