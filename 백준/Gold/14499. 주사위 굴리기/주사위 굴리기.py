dice=[0,0,0,0,0,0]
N,M,x,y,k = map(int, input().split())
diceMaps=[[0] * M for _ in range(N)]
commands=[]
answer=[]

def checkOutside(direction):
    if direction==1 and y==M-1:
        return False
    elif direction==2 and y==0: 
        return False
    elif direction==3 and x==0: 
        return False
    elif direction==4 and x==N-1: 
        return False
    else:
        return True
            

def turnDice(direction):
    # 동쪽
    global dice,x,y
    new_dice=[]
    if direction==1:
        new_dice=[dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
        dice=new_dice
        y+=1
    # 서쪽
    elif direction==2:
        new_dice=[dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
        dice=new_dice
        y-=1
    # 북쪽
    elif direction==3:
        new_dice=[dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
        dice=new_dice
        x-=1
    # 남쪽
    elif direction==4:
        new_dice=[dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
        dice=new_dice
        x+=1

    if diceMaps[x][y]==0:
        diceMaps[x][y]=dice[5]
    else :
        dice[5]=diceMaps[x][y]
        diceMaps[x][y]=0
    print(dice[0])

for i in range(N):
    row_values = list(map(int, input().split()))
    for j in range(M):
        diceMaps[i][j] = row_values[j]

commands=list(map(int, input().split()))


for i in commands:
    if checkOutside(i)==False:
        continue
    turnDice(i)
