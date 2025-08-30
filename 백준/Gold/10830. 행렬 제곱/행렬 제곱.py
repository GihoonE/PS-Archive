import sys
input = sys.stdin.readline
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
MOD = 1000
def mat_mul(X, Y):
    n = len(X)
    Z = [[0]*n for _ in range(n)]
    YT = list(zip(*Y))
    for i in range(n):
        Xi = X[i]
        Zi = Z[i]
        for j in range(n):
            s = 0
            Yj = YT[j]
            for k in range(n):
                s = (s + Xi[k] * Yj[k]) % MOD
            Zi[j] = s
    return Z

def mat_pow(A, e):
    if e == 1:
        return [[x % MOD for x in row] for row in A]
    half = mat_pow(A, e // 2)
    res = mat_mul(half, half)
    if e % 2 == 1:
        res = mat_mul(res, A)
    return res

ans = mat_pow(A, B)
print("\n".join(" ".join(map(str, row)) for row in ans))