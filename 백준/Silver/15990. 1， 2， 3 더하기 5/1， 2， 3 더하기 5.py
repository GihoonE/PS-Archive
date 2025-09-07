import sys
T = int(sys.stdin.readline().strip())
MOD = 1_000_000_009
dp1, dp2, dp3 = [0] * (100001), [0] * (100001), [0] * (100001)
dp1[1] = 1
dp2[2] = 1
dp1[3], dp2[3], dp3[3] = 1, 1, 1
for i in range(4, 100001):
    dp1[i] = (dp2[i - 1] + dp3[i - 1])%MOD  # 끝이 1
    dp2[i] = (dp1[i - 2] + dp3[i - 2])%MOD  # 끝이 2
    dp3[i] = (dp1[i - 3] + dp2[i - 3])%MOD  # 끝이 3
for _ in range(T):
    coin = [1,2,3]
    tar = int(sys.stdin.readline().strip())
    dp = [[0]*4 for _ in range(5)]
    if tar == 1:
        print(1)
    elif tar == 2:
        print(1)
    elif tar == 3:
        print(3)
    else:
        print((dp1[tar] + dp2[tar] + dp3[tar])%MOD)
