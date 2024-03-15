from collections import defaultdict
answer=[]

def is_banned_user(user, banned):
    if len(user)!=len(banned): return False
    for i in range(len(user)):
        if banned[i]=='*': continue
        if user[i]!=banned[i]: return False
    return True

def dfs(candidate_arr, visitor, k):
    global answer
    if k==len(candidate_arr): 
        visitor = sorted(visitor)
        if visitor not in answer:
            answer.append(visitor)
        return
    for candidate in candidate_arr[k]:
        if candidate not in visitor:
            visitor.append(candidate)
            dfs(candidate_arr, visitor, k+1)
            visitor.pop()
        else:
            continue
        

def solution(user_id, banned_id):
    global answer
    candidate_arr=[]

    for banned in banned_id:
        candidate=[]
        for user in user_id:
            if is_banned_user(user, banned): 
                candidate.append(user) 
        candidate_arr.append(candidate)
    
    dfs(candidate_arr, [], 0)
    return len(answer)