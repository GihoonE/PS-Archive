import sys
input = sys.stdin.readline

a, b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(a)]
c, d = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(c)]
C = [[0]*d for _ in range(a)]
for i in range(a):
    for j in range(d):
        s = 0
        for k in range(b):
            s += A[i][k] * B[k][j]
        C[i][j] = s

print('\n'.join(' '.join(map(str, row)) for row in C))
