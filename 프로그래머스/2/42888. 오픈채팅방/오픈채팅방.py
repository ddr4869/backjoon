def solution(record):
    
    userRecord=[]
    for i in record:
        userRecord.append(i.split(" "))
    
    move=[userRecord[i][0] for i in range(len(record))] 

    nameMap={userRecord[i][1]:userRecord[i][2] for i in  range(len(record)) if move[i]=="Change" or move[i]=="Enter"}

    answer = []
    for i in userRecord:
        if i[0]=="Enter":
            answer.append(nameMap[i[1]]+"님이 들어왔습니다.")
        elif i[0]=="Leave":
            answer.append(nameMap[i[1]]+"님이 나갔습니다.")

    return answer