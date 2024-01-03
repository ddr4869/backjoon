
def solve(N, K, dist, cnt, here, min_dist):
    if cnt>K or cnt>min_dist[here]: return
    min_dist[here]=cnt
    for i in range(1,N+1):
        if dist[here][i]!=10001:
            solve(N, K, dist, cnt+dist[here][i], i, min_dist)

def solution(N, road, K):
    answer=0
    dist=[[10001 for _ in range(N+1)] for _ in range(N+1)]
    min_dist=[500001 for _ in range(N+1)]
    for info in road:
        dist[info[0]][info[1]]=min(info[2], dist[info[0]][info[1]])
        dist[info[1]][info[0]]=min(info[2], dist[info[1]][info[0]])
    solve(N,K,dist,0,1,min_dist)
    for i in range(1,N+1):
        if min_dist[i]<=K: answer+=1
    return answer