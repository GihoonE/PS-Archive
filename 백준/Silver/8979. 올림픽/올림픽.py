import sys
import heapq

N,tar = map(int,sys.stdin.readline().split())
arr = []
tar_g = -1
tar_s = -1
tar_b = -1
for _ in range(N):
    t,a,b,c = map(int,sys.stdin.readline().split())
    if t == tar:
        t = 1001
        tar_g = a
        tar_s = b
        tar_b = c
    arr.append((a,b,c,t))
arr.sort(key=lambda x: (-x[0],-x[1],-x[2]))
count = 0
start = False
for i in range(len(arr)-1,-1,-1):
    if arr[i][3] == 1001:
        start = True
    if start:
        if arr[i][0] != tar_g or arr[i][1] != tar_s or arr[i][2] != tar_b:
            count = i + 1
            break
print(count + 1)

