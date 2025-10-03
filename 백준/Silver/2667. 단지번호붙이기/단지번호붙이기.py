import sys
from collections import deque
N = int(sys.stdin.readline().strip())
dp = [[0]*(N+2)]
for _ in range(N):
    dp.append([0]+list(map(int,sys.stdin.readline().rstrip()))+[0])
dp.append([0]*(N+2))
visited = [[False]*(N+2) for _ in range(N+2)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    count = 1
    while q:
        cur_x,cur_y = q.popleft()
        for i in range(4):
            nex_x = cur_x + dx[i]
            nex_y = cur_y + dy[i]
            if not visited[nex_x][nex_y] and dp[nex_x][nex_y] == 1:
                visited[nex_x][nex_y] = True
                q.append((nex_x,nex_y))
                count += 1
    return count

ans = []
for i in range(1,N+1):
    for j in range(1,N+1):
        if not visited[i][j] and dp[i][j] == 1:
            ans.append(bfs(i,j))
print(len(ans))
print("\n".join(map(str,sorted(ans))))