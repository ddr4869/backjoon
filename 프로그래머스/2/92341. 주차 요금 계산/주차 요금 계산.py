def calcTime(inTime, outTime):
    hour=int(outTime[0:2])-int(inTime[0:2])
    min=int(outTime[3:5])-int(inTime[3:5])
    return hour*60+min

def solution(fees, records):
    answer = []
    inParking={}
    parkingTimesDict={}
    for record in records:
        time,number,inout=record.split(" ")
        if inout=="IN":
            inParking[number]=time
        else:         
            parkTime=calcTime(inParking[number], time)
            if number in parkingTimesDict:
                parkingTimesDict[number]+=parkTime
            else:
                parkingTimesDict[number]=parkTime
            inParking.pop(number)

    for number in inParking:
        parkTime=calcTime(inParking[number], "23:59")
        if number in parkingTimesDict:
            parkingTimesDict[number]+=parkTime
        else:
            parkingTimesDict[number]=parkTime

    parkingTimesDict=dict(sorted(parkingTimesDict.items()))
    for i in parkingTimesDict:
        totalTime=parkingTimesDict[i]
        if totalTime<=fees[0]:
            answer.append(fees[1])
            continue
        
        totalTime-=fees[0]
        if totalTime%fees[2]==0:
            answer.append(totalTime//fees[2]*fees[3]+fees[1])
        else:
            answer.append((totalTime//fees[2]+1)*fees[3]+fees[1])
    return answer