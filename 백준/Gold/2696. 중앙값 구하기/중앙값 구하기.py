import sys
import heapq as hp
N = int(sys.stdin.readline().strip())
for _ in range(N):
    a = int(sys.stdin.readline().strip())
    arr = []
    while len(arr) < a:
        arr += list(map(int,sys.stdin.readline().strip().split()))

    str = []
    count = 0
    for i in range(len(arr)):
        #i: 0  ~ a-1
        # num = arr[i]
        if not i&1:
            str.append(sorted(arr[0:i+1])[(i)//2])
            count += 1
    ret = ""
    print(count)
    for i in range(count):
        if i%10 == 0 and i != 0:
            ret +=  f"\n{str[i]} "
        else:
            ret += f"{str[i]} "
    print(ret)