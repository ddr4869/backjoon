def solution(numbers):
    for i,v in enumerate(numbers):
        numbers[i]=str(v)
    numbers.sort(reverse=True, key=lambda x:x*3)
    answer=str(int(''.join(numbers)))
    return answer