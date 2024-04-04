n,m = list(map(int, input().split()))
board=[[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    board[i]=list(map(int, input().split()))

tet=[
    [[0,0],[0,1],[0,2],[0,3]],
    [[0,0],[1,0],[0,1],[1,1]],
    [[0,0],[1,0],[2,0],[2,1]],
    [[0,0],[1,0],[1,1],[2,1]],
    [[0,0],[0,1],[0,2],[1,1]],
]

def adjust_locate(tet):
    tet.sort(key=lambda x:(x[1],x[0]))
    gap_y=tet[0][0]
    gap_x=tet[0][1]
    for i in range(4):
        tet[i][0]-=gap_y
        tet[i][1]-=gap_x
    return tet

def rotate(tet):
    dy,dx=[1,1,-1,-1],[1,-1,1,-1]
    ret=[]
    for i in range(4):
        ny,nx=dy[i],dx[i]
        rotate_tet=[[ny*y, nx*x] for y,x in tet]
        adjust_tet=adjust_locate(rotate_tet)
        if adjust_tet not in ret:
            ret.append(adjust_tet) 
    for i in range(4):
        ny,nx=dy[i],dx[i]
        rotate_tet=[[ny*x, nx*y] for y,x in tet]
        adjust_tet=adjust_locate(rotate_tet)
        if adjust_tet not in ret:
            ret.append(adjust_tet) 
    return ret

tets=[]
for i in tet:
    for t in rotate(i):
        tets.append(t)
answer=0
for i in range(n):
    for j in range(m):
        for te in tets:
            sum=0
            for t in te:
                if 0<=i+t[0]<n and 0<=j+t[1]<m:
                    sum+=board[i+t[0]][j+t[1]]
                else: break
            if sum>answer: answer=sum
print(answer)
