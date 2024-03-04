def gcd(a,b):
    if b>a: a,b=b,a
    if b==0: return a
    else: return gcd(b,a%b)      

def find_division(array):
    if len(array)==1:
        return array[0]
    division=gcd(array[0],array[1])
    for i in array[1:]:
        division=gcd(i,division)
    return division

def is_not_division(array, divisions):
    for arr in array:
        if arr%divisions==0: return 0
    return divisions
    
def solve(arrayA, arrayB):
    divisions=find_division(arrayA)
    answer=is_not_division(arrayB, divisions) if divisions else 0
    return answer
    
def solution(arrayA, arrayB):
    sorted(arrayA); sorted(arrayB)
    return max(solve(arrayA, arrayB), solve(arrayB, arrayA))
