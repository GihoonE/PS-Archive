import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    C = list(map(int,sys.stdin.readline().split()))
    dp = [[0]*(N+1) for _ in range(N+1)]
    psum = [0] * (N + 1)
    for i in range(N):
        psum[i + 1] = psum[i] + C[i]
    def interval_sum(l, r):
        return psum[r + 1] - psum[l]  # C[l] ~ C[r]
    for L in range(2,N+1): # L: 2 ~ N
        for i in range(0,N-L+1): # i: 0 ~ N-L
            #dp[i][j]: i~j번쨰 파일을 합쳤을때 최소값
            q = 10**(8)
            idx = -1
            for k in range(i,i+L-1):
                q = min(q,dp[i][k]+dp[k+1][i+L-1]+interval_sum(i,i+L-1))
            dp[i][i+L-1] = q
    print(dp[0][N-1])