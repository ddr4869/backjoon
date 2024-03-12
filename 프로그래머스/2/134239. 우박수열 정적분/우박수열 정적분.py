def calc_area(fa,fb):
    if fb>fa: fa,fb=fb,fa # fa is bigger than fb
    return (fb + 0.5*(fa-fb))

def solution(k, ranges):
    answer = [0] * len(ranges)
    graph=[k]
    n=0
    while(k>1):
        if (k%2): k= k*3+1
        else: k/=2
        n+=1
        graph.append(k)
    idx=0
    for rge in ranges:
        a,b=rge[0],n+rge[1]
        if a>b: answer[idx]=-1.0; idx+=1; continue
        if a>b: answer[idx]=0; idx+=1; continue
        sum=0
        for i in range(a,b):
            sum+=calc_area(graph[i],graph[i+1])
        answer[idx]=sum; idx+=1
    return answer