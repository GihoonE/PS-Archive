import sys
#dp[i] i번쨰 엘레멘트가 포함된 감소하는 수열의 최대길이
N = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().strip().split()))
dp = [1]*(N+1)
for i in range(1,N):
    for j in range(0,i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))