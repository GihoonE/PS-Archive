import sys
N = int(sys.stdin.readline().strip())
dp_max = [[0]*3 for _ in range(2)]
dp_min = [[0]*3 for _ in range(2)]
s = list(map(int,sys.stdin.readline().split()))
dp_max[0] = s[:]
dp_min[0] = s[:]
for i in range(1, N):
    s = list(map(int,sys.stdin.readline().split()))
    for j in range(3):
        if j == 0:
            dp_max[1][j] = s[j] + max(dp_max[0][0], dp_max[0][1])
            dp_min[1][j] = s[j] + min(dp_min[0][0], dp_min[0][1])
        elif j == 1:
            dp_max[1][j] = s[j] + max(dp_max[0][0], dp_max[0][1], dp_max[0][2])
            dp_min[1][j] = s[j] + min(dp_min[0][0], dp_min[0][1], dp_min[0][2])
        else:
            dp_max[1][j] = s[j] + max(dp_max[0][1], dp_max[0][2])
            dp_min[1][j] = s[j] + min(dp_min[0][1], dp_min[0][2])
    dp_max[0] = dp_max[1][:]
    dp_min[0] = dp_min[1][:]
print(max(dp_max[0]), min(dp_min[0]))