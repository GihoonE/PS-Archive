import sys
import heapq

N = int(sys.stdin.readline())
arr = [0]*(21)
for _ in range(N):
    input = sys.stdin.readline().strip()
    if input[0:3] == 'all':
        arr = [1]*(21)
    elif input[0:5] == 'empty':
        arr = [0]*(21)
    else:
        a,b = input.split()
        b = int(b)
        if a == 'add':
            arr[b] = 1
        elif a == 'remove':
            arr[b] = 0
        elif a == 'toggle':
            arr[b] =  1^arr[b]
        else:
            print(arr[b])