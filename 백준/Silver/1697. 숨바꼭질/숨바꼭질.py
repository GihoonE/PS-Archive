import sys
from collections import deque
S, E = map(int, sys.stdin.readline().split())
MAX = 100000
dp = [float('inf')] * (MAX + 1)
dp[S] = 0

q = deque([S])

while q:
    cur = q.popleft()
    for nxt in (cur - 1, cur + 1, cur * 2):
        if 0 <= nxt <= MAX and dp[cur] + 1 < dp[nxt]:
            dp[nxt] = dp[cur] + 1
            q.append(nxt)

print(dp[E])