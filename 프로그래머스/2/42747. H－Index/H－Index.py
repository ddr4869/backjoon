def solution(citations):
    citations.sort(reverse=True)
    target=citations[0]
    idx=0
    while(target):
        while(idx<len(citations) and citations[idx]>=target):
            idx+=1
        if idx>=target and len(citations)-idx<=target:
            return target
        target-=1
    return 0