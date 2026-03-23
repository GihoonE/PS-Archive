import sys
input = sys.stdin.readline
while True:
    arr = list(map(int,input().split()))
    if arr[0] == 0:
        break
    else:
        N,arr = arr[0], arr[1:]+[0]
        ans = 0
        s = [0]
        for i in range(1,len(arr)):
            while s and arr[s[-1]] > arr[i]:
                cur = s.pop()
                if s:
                    left = s[-1]
                else:
                    left = -1
                width = i - left - 1
                ans = max(ans, width*arr[cur])
            s.append(i)
        print(ans)