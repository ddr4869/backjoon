def timeConvert(start, end):
    return 60*(int(end[0:2])-int(start[0:2]))+int(end[3:5])-int(start[3:5])

def convertMelody(melody):
    melody=melody.replace("C#","c")
    melody=melody.replace("D#","d")
    melody=melody.replace("F#","f")
    melody=melody.replace("G#","g")
    melody=melody.replace("A#","a")
    return melody
    
def solution(m, musicinfos):
    
    m=convertMelody(m)
    melody_len=len(m)
    answerList=[]
    
    for mdstr in musicinfos:
        md=mdstr.split(',')
        thisMelody=convertMelody(md[3])
        time=timeConvert(md[0],md[1])
        if time < melody_len:
            continue
            
        thisMelodyLen=len(thisMelody)
        thisMelody*= (melody_len//thisMelodyLen+2)
        start=thisMelody.find(m)
        print(start)
        if start==-1:
            continue
        if start+melody_len<=time+1:
            answerList.append([md[2],time,md[0]])

    if not answerList:
        return "(None)"
    return sorted(answerList, key= lambda x: (-int(x[1]),x[2]))[0][0]