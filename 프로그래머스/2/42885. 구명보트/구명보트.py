def solution(people, limit):
    answer = 0
    people.sort()
    left,right=0,len(people)-1
    on_boat,total=0,0
    
    while(left<=right):
        if on_boat==0:
            total+=people[right]
            right-=1
            on_boat+=1
        else:
            if total+people[left]<=limit:
                left+=1
            total=0
            on_boat=0
            answer+=1
    return answer+on_boat