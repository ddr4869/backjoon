def solution(sequence, k):
    length=len(sequence)
    left,right=length-1,length-1
    sum=sequence[right]

    while(left>=0 and right>=0):
        if sum>k:
            sum-=sequence[right]
            right-=1
        elif sum==k:
            if left-1>=0 and sequence[right]==sequence[left-1]:
                right-=1; left-=1
            else:
                return [left,right]
        else:
            left-=1
            sum+=sequence[left]
