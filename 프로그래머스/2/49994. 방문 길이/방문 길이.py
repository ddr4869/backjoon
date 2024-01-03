def solution(dirs):
    walk={}
    y,x=0,0
    for i in dirs:
        if y==5 and i=='U': continue
        if y==-5 and i=='D': continue
        if x==5 and i=='R': continue
        if x==-5 and i=='L': continue
        if i=='U':
            key="y"+str(y)+str(y+1)+str(x)
            walk[key]=True
            y+=1
        elif i=='D': 
            key="y"+str(y-1)+str(y)+str(x)
            walk[key]=True
            y-=1
        elif i=='R':
            key="x"+str(x)+str(x+1)+str(y)
            walk[key]=True
            x+=1
        elif i=='L': 
            key="x"+str(x-1)+str(x)+str(y)
            walk[key]=True
            x-=1
    return len(walk)