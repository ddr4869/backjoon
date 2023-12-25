from itertools import product
Users,Emoticons = [],[]
emoticon_len=0

def calculate(discount_list):
    global Users, Emoticons, emoticon_len
    total_price, plus_cnt=0,0
    Users_len=len(Users)
    users_const_sum=[0 for _ in range(Users_len)]

    for emoji_idx in range(emoticon_len):
        for user_idx in range(Users_len):
            if (Users[user_idx][0]<=discount_list[emoji_idx]):
                users_const_sum[user_idx]+= Emoticons[emoji_idx]*(100-discount_list[emoji_idx])//100
            

    total_price=sum(users_const_sum)

    for idx, users_sum in enumerate(users_const_sum):

        if users_sum>=Users[idx][1]:
            plus_cnt+=1
            total_price-=users_const_sum[idx]

    return total_price, plus_cnt



def solution(users, emoticons):
    global Users, Emoticons, emoticon_len
    Users=users
    Emoticons=emoticons
    emoticon_len=len(emoticons)

    discount_cases = [list(combination) for combination in product([10, 20, 30, 40], repeat=emoticon_len)]

    max_price,max_plus = 0,0

    for discount_list in discount_cases:
        price,plus=calculate(discount_list)
        if plus>max_plus:
            max_price=price
            max_plus=plus
        elif plus==max_plus:
            max_price=max(max_price,price)


    return [max_plus, max_price]