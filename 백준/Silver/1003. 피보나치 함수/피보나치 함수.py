import sys
T = int(sys.stdin.readline().strip())
dp = [[-1,-1] for _ in range(41)]
dp[0] = [1,0]
dp[1] = [0,1]
def fib(N):
    if dp[N][0] == -1 and dp[N][1] == -1:
        n1 = fib(N-1)
        n2 = fib(N-2)
        dp[N] = [n1[0]+n2[0],n1[1]+n2[1]]
        return dp[N]
    else:
        return dp[N]

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    ret = fib(N)
    print(f'{ret[0]} {ret[1]}')