A, B = map(int, input().split())
answer=-1

def Calclate(number, cnt):
    global answer
    if number>B:
        return
    if number==B:
        answer=cnt
        return
    Calclate(number*2, cnt+1)
    Calclate(10*number+1, cnt+1)

Calclate(A, 1)
print(answer)