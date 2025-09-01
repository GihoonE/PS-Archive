import sys
import heapq as hp
pos = []
neg = []
N = int(sys.stdin.readline().strip())
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if len(pos) == 0 and len(neg) == 0:
            print(0)
        elif len(pos) == 0:
            print(-1*hp.heappop(neg))
        elif len(neg) == 0:
            print(hp.heappop(pos))
        else:
            if neg[0] <= pos[0]:
                print(-1*hp.heappop(neg))
            else:
                print(hp.heappop(pos))
    else:
        if num < 0:
            hp.heappush(neg,abs(num))
        else:
            hp.heappush(pos,num)