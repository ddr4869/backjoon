def solution(cards):
    visited = [0] * len(cards)
    scores=[]

    for i,_ in enumerate(cards):
        cards[i]-=1

    for i in range(len(cards)):
        if visited[i]==0:
            target,cnt=i,0
            while(visited[target]==0):
                visited[target]=1
                cnt+=1
                target=cards[target]
            scores.append(cnt)

    scores.sort()
    return scores[-1]*scores[-2] if len(scores)>=2 else 0