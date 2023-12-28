import math

def number_to_binary(num):
    ans=""
    while (num):
        ans=str(num%2)+ans
        num//=2
    return '0'+ans

def binary_to_num(binary, binary_len):
    sum=0
    start=1
    idx=binary_len-1
    while(idx>=0):
        if binary[idx]=='1':
            sum+=start
        start*=2
        idx-=1
    return sum

def calc_result(binary):
    binary_len=len(binary)
    idx=binary_len-1
    while(idx>=0 and binary[idx]=='1'):
        idx-=1
    
    binary=list(binary)
    binary[idx]='1'
    if idx+1<binary_len:
        binary[idx+1]='0'

    return binary_to_num(binary,binary_len)

def solution(numbers):
    answer = []
    for number in numbers:
        if number==1:
            answer.append(2)
            continue
        binary=number_to_binary(number)
        answer.append(calc_result(binary))
        
    return answer