zero=0
one=0
def seperate(arr, n, y, x):
    global zero, one
    num=arr[y][x]
    flag=False
    for i in range(n):
        for j in range(n):
            if arr[y+i][x+j]!=num:
                seperate(arr, n//2, y, x)
                seperate(arr, n//2, y+n//2, x)
                seperate(arr, n//2, y, x+n//2)
                seperate(arr, n//2, y+n//2, x+n//2)
                return
    if num: one+=1
    else: zero+=1  

def solution(arr):
    global zero, one
    answer = []
    n=len(arr)
    seperate(arr,n,0,0)
    answer.append(zero)
    answer.append(one)
    return answer