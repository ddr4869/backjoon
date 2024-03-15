def solution(sticker):
    if len(sticker)==1: return sticker[0]
    if len(sticker)==2: return max(sticker[0],sticker[1])
    dp=[0 for _ in range(len(sticker))]
    dp[0]=sticker[0]
    dp[1]=max(sticker[0], sticker[1])
    for i in range(2,len(sticker)-1):
        dp[i]=max(dp[i-2]+sticker[i], dp[i-1])
    
    dp2=[0 for _ in range(len(sticker))]
    dp2[1]=sticker[1]
    dp2[2]=max(sticker[1], sticker[2])
    for i in range(3,len(sticker)):
        dp2[i]=max(dp2[i-2]+sticker[i], dp2[i-1])

    return max(dp[-2],dp2[-1])