from itertools import permutations
from collections import defaultdict
import math

def isPirme(num):
    if num<=1: return False
    end=int(math.sqrt(num))+1
    for i in range(2,end):
        if (num%i)==0:
            return False
    return True

def solution(numbers):
    answer = 0
    idx=1
    flag=defaultdict(int)
    while(idx<=len(numbers)):
        perm=permutations(numbers, idx)
        for i in perm:
            num=int(''.join(i))
            if flag[num]==0 and isPirme(num): 
                answer+=1
                flag[num]=1
        idx+=1

    return answer