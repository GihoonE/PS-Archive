import sys
import heapq

N = int(sys.stdin.readline())
for _ in range(N):
    input = list(map(int,sys.stdin.readline().split()))
    t = input[0]
    temp = [input[1]]
    count = 0
    for i in range(2,len(input)):
        cur = input[i]
        if temp[-1] < cur:
            temp.append(cur)
        else:
            for j in range(len(temp)):
                if cur < temp[j]:
                    count += len(temp) - j
                    temp.insert(j,cur)
                    break
    print(f'{t} {count}')
