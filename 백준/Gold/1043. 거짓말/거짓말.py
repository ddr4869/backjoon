import sys
input = sys.stdin.readline
n,m = list(map(int, input().split()))
real=list(map(int, input().split()))
real=real[1:]
parties=[]
for i in range(m):
    peoples=list(map(int, input().split()))
    parties.append(peoples[1:])

flag=True
while(flag):
    flag=False
    have_real_people=[]
    for party in parties:
        for people in party:
            if people in real:
                for people in party:
                    if people not in real: real.append(people)
                have_real_people.append(party)
                flag=True
                break
    parties=[party for party in parties if party not in have_real_people]
print(len(parties))