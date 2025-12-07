import sys
from collections import deque
N,Q = map(int,sys.stdin.readline().split())
dp = [[] for _ in range(N+1)]

for _ in range(N-1):
    p,q,r = map(int,sys.stdin.readline().split())
    dp[p].append((q,r))
    dp[q].append((p,r))

for _ in range(Q):
    k,v = map(int,sys.stdin.readline().split())
    count = 0
    q = deque()
    q.append(v)
    visited = [False]*(N+1)
    visited[v] = True
    while q:
        current_node = q.popleft()
        for next_node,k_value in dp[current_node]:
            if k_value >= k and not visited[next_node]:
                count += 1
                visited[next_node] = True
                q.append(next_node)
    print(count)