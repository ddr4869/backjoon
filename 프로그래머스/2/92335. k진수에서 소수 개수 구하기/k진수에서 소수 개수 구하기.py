from collections import deque
def isPrime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if i*i>n:
            return True
        if n%i==0:
            return False
    return True
        

def solution(n, k):
    primeDeque=deque()
    while(n):
        primeDeque.appendleft(n%k)
        n=n//k
    primeList=list(primeDeque)
    primes=[]
    idx,primeNumber=0,0
    while(idx>=len(primeList)):
        if printList(idx)==0:
            primes.append(primeNumber)
            primeNumber=0
            idx+=1
        primeNumber*=10
        primeNumber+=printList(idx)
    if primeNumber!= 0:
        printList.append(primeNumber)
      
    answer = 0
    for prime in primeList:
        if isPrime(prime):
            answer+=1
    
    return answer