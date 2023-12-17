from itertools import combinations
from collections import Counter
def solution(orders, course):
    
    answer = []
    
    courseCounter=Counter()
    
    for numberOfCourse in course:
        courseCounter=Counter()
        thisCounter=Counter()
        for order in orders:
            orderList=list(order)
            orderList.sort()
            orderComb=list(combinations(orderList, numberOfCourse))
            courseCounter+=Counter(orderComb)
            
        #print(courseCounter)
        if len(courseCounter)==0:
            continue
        
        
        mostNumber=courseCounter.most_common()[0][1]
        if mostNumber==1:
            continue
        #print(mostNumber)
        for cntPair in courseCounter.most_common():
            if courseCounter[cntPair[0]]==mostNumber:
                answer.append(''.join(cntPair[0]))
            else:
                break
        
    answer.sort()
    return answer