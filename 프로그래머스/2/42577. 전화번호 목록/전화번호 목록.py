def solution(phone_book):
    numbers={}
    for number in phone_book:
        numbers[number]=True
    for number in phone_book:
        prefix=''
        for i in number:
            if prefix in numbers: return False
            prefix+=i
    return True