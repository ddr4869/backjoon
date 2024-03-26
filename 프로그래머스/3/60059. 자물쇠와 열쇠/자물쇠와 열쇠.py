def adjust_locate(key_location):
    min_y,min_x_list=10e5,[]
    for i in range(len(key_location)):
        min_y=min(min_y,key_location[i][0])
    for i in range(len(key_location)):
        if key_location[i][0]==min_y:
            min_x_list.append(key_location[i][1])
    min_x=min(min_x_list)
    for i in range(len(key_location)):
        key_location[i][0]-=min_y
        key_location[i][1]-=min_x
    return key_location

def rotate_key(key_location_set, key_location):
    key_location=adjust_locate(key_location)
    left_key_location=[]
    up_key_location=[]
    diagonal_key_location=[]
    for i in range(len(key_location)):
        left_key_location.append([-key_location[i][1],key_location[i][0]])
        diagonal_key_location.append([-key_location[i][0],-key_location[i][1]])
        up_key_location.append([key_location[i][1],-key_location[i][0]])
    key_location_set.append(key_location)
    key_location_set.append(adjust_locate(left_key_location))
    key_location_set.append(adjust_locate(diagonal_key_location))
    key_location_set.append(adjust_locate(up_key_location))
    return key_location_set

def solution(key, lock):
    answer = True
    n=len(key)
    m=len(lock)
    key_location=[]
    for i in range(n):
        for j in range(n):
            if key[i][j]==1:
                key_location.append([i,j])
    key_location_set=[]
    key_location_set=rotate_key(key_location_set, key_location)

    hole_cnt=0
    for i in range(m):
        for j in range(m):
            if lock[i][j]==0: hole_cnt+=1

    def can_open(i, j):
        for key_location in key_location_set:
            cnt=0
            _pass=True
            for y,x in key_location:
                if 0<=i+y<m and 0<=j+x<m:
                    if lock[i+y][j+x]==1: 
                        _pass=False; break
                    else: cnt+=1
            if _pass and cnt==hole_cnt: return True
        return False

    for i in range(2*n+m):
        for j in range(2*n+m):
            if can_open(-n+i,-n+j):
                return True
    return False 