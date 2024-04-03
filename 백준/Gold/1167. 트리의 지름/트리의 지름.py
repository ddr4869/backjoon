import sys
from collections import defaultdict
input = sys.stdin.readline
n=int(input())
link=defaultdict(list)
for i in range(n):
    info=list(map(int, input().split()))
    node=info[0]
    dist=info[1:-1]
    for j in range(0,len(dist),2):
        link[node].append((dist[j+1],dist[j]))    

answer=0
visited=[0 for _ in range(n+1)]
def dfs(here, visited, cost):
    global answer
    if visited[here]!=0: return 0
    visited[here]=1
    answers=[]
    for next_cost, _next in link[here]:
        if visited[_next]==0:
            ans=dfs(_next, visited, cost)+next_cost
            if len(answers)==0: answers.append(ans)
            elif len(answers)==1:
                if answers[0]<ans: answers=[ans,answers[0]]
                else: answers.append(ans)
            else:
                if answers[0]<ans: answers=[ans,answers[0]]
                elif answers[0]>=ans>answers[1]: answers[1]=ans
    if len(answers)==2 and sum(answers)>answer: answer=sum(answers)
    ret=answers[0]+cost if answers else cost        
    if ret>answer: answer=ret
    return ret

dfs(1,visited,0)
print(answer)