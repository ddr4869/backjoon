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
    answers=[]
    if visited[here]!=0: return 0
    visited[here]=1
    for next_cost, _next in link[here]:
        if visited[_next]==0:
            ans=dfs(_next, visited, cost)+next_cost
            answers.append(ans) 
    if answers: 
        answers.sort(reverse=True)
        if len(answers)>=2: 
            answer=max(answer,answers[0]+answers[1])
        else: answer=max(answer,answers[0])
    return answers[0]+cost if answers else cost        

dfs(1,visited,0)
print(answer)