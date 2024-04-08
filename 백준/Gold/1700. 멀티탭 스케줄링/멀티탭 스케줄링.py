import sys
from collections import deque
input = sys.stdin.readline
n,k=list(map(int, input().split()))
order=list(map(int, input().split()))

def find_latest(q, target_idx):
    latest=-1; ret=0
    left_list=order[target_idx+1:]
    for i in q:
        if i not in left_list: return i
        idx=left_list.index(i)
        if idx>latest: 
            latest=idx
            ret=i
    return ret

answer=0
q=set()
for target_idx,target in enumerate(order):
    if len(q)<n: q.add(target)
    else:
        if target in q: continue
        q.remove(find_latest(q, target_idx))
        q.add(target)
        answer+=1
print(answer)