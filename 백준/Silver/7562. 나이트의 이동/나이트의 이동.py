import sys
from collections import deque
T = int(sys.stdin.readline().strip())
for _ in range(T):
    L = int(sys.stdin.readline().strip())
    dp = [[float('inf')]*L for _ in range(L)]
    visited = [[False]*L for _ in range(L)]
    s = tuple(map(int,sys.stdin.readline().split()))
    e = tuple(map(int,sys.stdin.readline().split()))
    q = deque()
    q.append(s)
    dp[s[1]][s[0]] = 0
    visited[s[1]][s[0]] = True
    dx = [-2,-2,-1,-1, 1, 1, 2, 2]
    dy = [-1, 1,-2, 2,-2, 2,-1, 1]
    while q:
        cx,cy = q.popleft()
        if cx == e[0] and cy == e[1]:
            break
        for i in range(len(dx)):
            nx,ny = cx+dx[i],cy+dy[i]
            if 0 <= nx <= L-1 and 0 <= ny <= L-1:
                if not visited[ny][nx] and dp[cy][cx]+1 < dp[ny][nx]:
                    visited[ny][nx] = True
                    dp[ny][nx] = dp[cy][cx] + 1
                    q.append((nx,ny))
    print(dp[e[1]][e[0]])