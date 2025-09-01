import sys
import heapq as hp
arr = []
N = int(sys.stdin.readline().strip())
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(hp.heappop(arr))
    else:
        hp.heappush(arr,num)