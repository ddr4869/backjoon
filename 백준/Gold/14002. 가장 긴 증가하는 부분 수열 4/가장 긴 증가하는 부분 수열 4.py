import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
minimums=[]
records=[]
for num in arr:
    if not minimums:
        minimums.append(num)
        records.append([num])
        continue
    if minimums[-1] < num:
        minimums.append(num)
        records.append(records[-1]+[num])
    else:
        idx = bisect_left(minimums, num)
        minimums[idx] = num
        if idx == 0:
            records[idx] = [num]
        else:
            records[idx] = records[idx-1]+[num]

print(len(records))
print(' '.join(map(str, records[-1])))