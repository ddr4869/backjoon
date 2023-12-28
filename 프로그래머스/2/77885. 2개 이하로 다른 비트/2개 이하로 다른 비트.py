import math

def calc_result(binary):
    binary_len=len(binary)
    idx=binary_len-1
    while(idx>=0 and binary[idx]=='1'):
        idx-=1
    
    binary=list(binary)
    binary[idx]='1'
    if idx+1<binary_len:
        binary[idx+1]='0'
    binary=''.join(binary)
    return int(binary,2)

def solution(numbers):
    answer = []
    for number in numbers:
        if number==1:
            answer.append(2)
            continue
        binary='0'+bin(number)[2:]
        answer.append(calc_result(binary))
    return answer