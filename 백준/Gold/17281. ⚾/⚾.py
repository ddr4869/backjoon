import sys
from itertools import permutations
input = sys.stdin.readline
n=int(input())
player_info=[]
for i in range(n):
    player_info.append(list(map(int, input().split())))
answer=0

for perm in list(permutations(range(1,9), 8)):
    player_idx=0; score=0
    order=list(perm[:3])+[0]+list(perm[3:])
    for inning in range(n):
        b1,b2,b3=0,0,0; out=0; 
        while(out<3):
            if player_info[inning][order[player_idx]]==0: out+=1
            else: 
                hit=player_info[inning][order[player_idx]]
                if hit==1: 
                    score+=b3
                    b3,b2,b1=b2,b1,1
                elif hit==2:
                    score+=b3+b2
                    b3,b2,b1=b1,1,0
                elif hit==3:
                    score+=b3+b2+b1
                    b3,b2,b1=1,0,0
                elif hit==4:
                    score+=b3+b2+b1+1
                    b3,b2,b1=0,0,0
            player_idx+=1
            if player_idx==9: player_idx=0
    answer=max(answer,score)
print(answer)