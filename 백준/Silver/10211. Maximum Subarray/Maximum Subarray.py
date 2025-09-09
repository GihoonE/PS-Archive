import sys
from collections import deque
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    arr = list(map(int,sys.stdin.readline().split()))
    dp = [[-1001]*(N) for _ in range(N)]

    # 길이 1 구간 초기화
    for i in range(N):
        dp[i][i] = arr[i]

    for L in range(2,N+1):
        for i in range(0,N-L+1):
            j = i + L - 1
            dp[i][j] = max(dp[i][j-1] + arr[j], dp[i][j])
    q = -1001
    for i in range(len(dp)):
        row_max = max(dp[i])
        if q < row_max:
            q = row_max
    print(q)