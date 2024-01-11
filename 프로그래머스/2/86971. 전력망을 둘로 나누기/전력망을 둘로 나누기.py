from collections import defaultdict

def solution(n, wires):
    answer = 100
    link=defaultdict(list)
    for a,b in wires:
        link[a].append(b)
        link[b].append(a)

    def calc(node, _from, link, visited):
        visited[node]=1
        network=link[node]
        cnt=1
        for _next in network:
            if _next==_from or visited[_next]==1: continue
            cnt+=calc(_next, node, link, visited)
        return cnt

    for _from, _to in wires:
        visited=[0 for _ in range(n+1)]
        from_total=calc(_from, _to, link, visited)
        to_total=n-from_total
        gap=from_total-to_total
        if gap<0: gap*=-1
        answer=min(answer, gap)

    return answer