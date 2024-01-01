from itertools import permutations
def solution(expression):
    answer = 0
    tmp=0
    seperatedExpression=[]
    symbol=[]
    for v in expression:
        if v.isnumeric():
            tmp*=10
            tmp+=int(v)
        else:
            seperatedExpression.append(tmp)
            tmp=0
            seperatedExpression.append(v)
            if v not in symbol:
                symbol.append(v)
            
    seperatedExpression.append(tmp)
    symbolPerm=permutations(symbol)

    for symbols in symbolPerm:
        thisExpression=seperatedExpression[:]
        for symbol in symbols:
            for idx,express in enumerate(thisExpression):
                if express==symbol:
                    if express=='-': calc=thisExpression[idx-1]-thisExpression[idx+1]
                    elif express=='+': calc=thisExpression[idx-1]+thisExpression[idx+1]
                    elif express=='*': calc=thisExpression[idx-1]*thisExpression[idx+1]
                    thisExpression[idx+1]=calc
                    thisExpression[idx-1],thisExpression[idx]='',''
            thisExpression=[i for i in thisExpression if i != '']
        answer=max(answer,abs(thisExpression[0]))
    return answer
