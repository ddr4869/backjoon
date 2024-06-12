import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
minimums=[]
history=[]
answer=[]
answer=1

for i, num in enumerate(arr):
    if not minimums:
        minimums.append(num)
        history.append([num,1])
        continue
    if minimums[-1] < num:
        minimums.append(num)
        history.append([num ,len(minimums)])
        answer=len(minimums)
    else:
        idx = bisect_left(minimums, num)
        if idx==0:
            history.append([num,1])
        else:
            #history.append([num, history[idx-1][1]+1])
            history.append([num, idx+1])
        minimums[idx] = num

print(len(minimums))
idx=0
seq = []
target_stack = 0
target_val = 0

for i in range(len(history)-1, -1, -1):
    if history[i][1] == answer:
        idx = i
        target_val = history[i][0]+1
        target_stack = history[i][1]
        break

while(target_stack and idx>=0):
    if target_stack == history[idx][1] and target_val > history[idx][0]:
        target_stack -= 1
        target_val = history[i][0]
        seq.append(history[idx][0])
    idx -= 1

print(' '.join(map(str, seq[::-1])))