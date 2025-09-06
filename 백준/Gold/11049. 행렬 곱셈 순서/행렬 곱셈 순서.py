import sys
N = int(sys.stdin.readline().strip())
A = []
dp = [[0]*N for _ in range(N)]
for _ in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))
for L in range(2,N+1): #구간 길이
    for i in range(0,N-L+1): #구간 시작
        j = i+L - 1 #구간 끝
        q = 10**18
        p1 = A[i][0]
        p2 = A[j][1]
        for k in range(i,j):
            q = min(dp[i][k]+ dp[k+1][j] + p1*A[k][1]*p2, q)
        dp[i][j] = q
print(dp[0][N-1])