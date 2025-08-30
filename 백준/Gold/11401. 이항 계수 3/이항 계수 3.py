import sys
a,b = map(int,sys.stdin.readline().strip().split())
mod = 1_000_000_007
dp = [1]*(a+1)
for i in range(2,a+1):
    dp[i] = dp[i-1]*i%mod

#invfac[a] = (a!)^(MOD-2) mod MOD  (Fermat)
inv = [1]*(a+1)
inv[a] = pow(dp[a],mod-2,mod)
for i in range(a,0,-1):
    inv[i-1] = inv[i]*i%mod
print(dp[a]*(inv[b]*inv[a-b]%mod)%mod)