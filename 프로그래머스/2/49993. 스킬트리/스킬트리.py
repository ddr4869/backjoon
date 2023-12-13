

def solution(skill, skill_trees):
    ranking={}
    answer = 0
    for idx,val in enumerate(skill):
        ranking[val]=idx
    
    for skill_tree in skill_trees:
        isRight=True
        idx=0
        for i in skill_tree:
            if i in ranking:
                if ranking[i]!=idx:
                    isRight=False
                    break
                else:
                    idx+=1
        if isRight:
            answer+=1
            print(skill_tree)

    return answer
