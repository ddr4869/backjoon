from collections import defaultdict
import heapq
def solution(n, s, a, b, fares):
    link=defaultdict(list)
    for start,arrive,cost in fares:
        link[start].append((arrive,cost))
        link[arrive].append((start,cost))
    
    def calc_distance(_from,_to):
        if _from==_to: return 0
        dp=[10e10 for _ in range(n+1)]
        ans=[]
        stack=[]
        stack.append((_from,0))
        while(stack):
            now,cost=heapq.heappop(stack)
            if now==_to: 
                ans.append(cost)
                continue
            if dp[now]<cost: continue
            _next_list=link[now]
            for _next,_next_cost in _next_list:
                if cost+_next_cost >= dp[_next]: continue
                dp[_next]=cost+_next_cost
                heapq.heappush(stack,(_next,cost+_next_cost))
        return min(ans) if ans else -1
    
    answer=10e10
    for i in range(1,n+1):
        StoI=calc_distance(s,i)
        if StoI==-1: continue
        ItoA=calc_distance(i,a)
        ItoB=calc_distance(i,b)
        answer=min(answer, StoI+ItoA+ItoB)
    return answer