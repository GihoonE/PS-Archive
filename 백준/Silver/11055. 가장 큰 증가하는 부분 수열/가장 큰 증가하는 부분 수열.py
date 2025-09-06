import sys
N = int(sys.stdin.readline().strip())
#dp[i] : ith element로 끝나는 증가부분 수열의 최대
arr = list(map(int,sys.stdin.readline().strip().split()))
dp = [0]*N
for i in range(0,len(arr)):
    dp[i] = arr[i]
    for j in range(0,i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],arr[i]+dp[j])
print(max(dp))