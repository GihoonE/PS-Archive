import sys
import heapq

N = int(sys.stdin.readline().strip())
arr = []
for _ in range(N):
    arr.append(tuple(map(int,sys.stdin.readline().split())))
str = ""
for i in range(N):
    cur_x, cur_y = arr[i][0], arr[i][1]
    count = 1
    for j in range(N):
        if i != j:
            if cur_x < arr[j][0] and cur_y < arr[j][1]:
                count += 1
    str += f'{count} '
print(str)
