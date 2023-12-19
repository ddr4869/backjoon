def Manhattan(place,y,x,dist):
    if dist>=3 or x>=5 or y>=5 or x<0 or y<0:
        return True
    if place[y][x]=='X':
        return True
    if dist!=0 and place[y][x]=='P':
        return False
    if Manhattan(place,y+1,x,dist+1) and Manhattan(place,y,x+1,dist+1):
        return True
    else:
        return False
        
def LeftUp(place,y,x):
    if y+1>=5 or x-1<0:
        return True
    if place[y][x-1]==place[y+1][x]=='X':
        return True
    if place[y+1][x-1]!='P':
        return True
    
    return False

def solution(places):
    answer = []
    for place in places:
        flag=True
        for y in range(5):
            for x in range(5):
                  if place[y][x]=='P':
                        if not Manhattan(place,y,x,0) or not LeftUp(place,y,x):
                            flag=False
                            break
            if flag==False:
                answer.append(0)
                break
        if flag==True:
            answer.append(1)             
    return answer