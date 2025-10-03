import sys
from collections import deque
T = int(sys.stdin.readline().strip())
for _ in range(T):
    V,E = map(int,sys.stdin.readline().split())
    dp = [[] for _ in range(V+1)]
    for _ in range(E):
        a,b = map(int,sys.stdin.readline().split())
        dp[a].append(b)
        dp[b].append(a)

    color = [0] * (V + 1) 
    is_bipartite = True

    for start in range(1, V + 1):
        if color[start] == 0:
            q = deque([start])
            color[start] = 1
            while q and is_bipartite:
                cur = q.popleft()
                for nxt in dp[cur]:
                    if color[nxt] == 0:
                        color[nxt] = -color[cur]
                        q.append(nxt)
                    elif color[nxt] == color[cur]:
                        is_bipartite = False
                        break

    print("YES" if is_bipartite else "NO")