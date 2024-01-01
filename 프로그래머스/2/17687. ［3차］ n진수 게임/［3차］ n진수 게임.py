from collections import deque
def calcBaseNumber(n, k): #n진법, 숫자 k
    number=deque()
    while(k):
        number.appendleft(k%n)
        k= k//n
    numberList=list(number)
    numberStr=""
    # print(numberList)

    for i,v in enumerate(numberList):
        if v>=10:
            numberStr+=chr(v+55)
        else:
            numberStr+=str(v)
    return numberStr if numberStr else "0"
    

def solution(n, t, m, p):
    # n:진법 t:숫자개수 m:참가인원 p:순서
    answer=''
    num,answer_len=0,0
    totalStr = ''
    while len(totalStr)<=t*m:
        #print(totalStr)
        totalStr+=calcBaseNumber(n,num)
        num+=1
    
    for i,v in enumerate(totalStr):
        if len(answer)==t:
            return answer
        if i%m==(p-1):
            answer+=v
    return answer