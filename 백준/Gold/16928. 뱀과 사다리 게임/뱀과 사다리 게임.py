import sys
from collections import deque
L, S = map(int, sys.stdin.readline().split())
jump = {}
for _ in range(L+S):
    a, b = map(int, sys.stdin.readline().split())
    jump[a] = b

dp = [-1] * 101
dp[1] = 0
q = deque([1])

while q:
    pos = q.popleft()
    for dice in range(1, 7):
        nxt = pos + dice
        if nxt > 100:
            continue
        if nxt in jump:
            nxt = jump[nxt]
        if dp[nxt] == -1:
            dp[nxt] = dp[pos] + 1
            q.append(nxt)
        if nxt == 100:
            break

print(dp[100])
