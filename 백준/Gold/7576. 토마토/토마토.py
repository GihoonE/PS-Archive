import sys
from collections import deque
N,M = map(int,sys.stdin.readline().strip().split())
dp = []
q = deque()
for i in range(M):
    row = list(map(int,sys.stdin.readline().split()))
    dp.append(row)
    for j in range(N):
        if row[j] == 1:
            q.append((i,j))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while q:
    cy,cx = q.popleft()
    for i in range(4):
        ny,nx = cy+dy[i],cx+dx[i]
        if 0 <= ny <= M-1 and 0 <= nx <= N-1:
            if dp[ny][nx] == 0:
                dp[ny][nx] = dp[cy][cx] + 1
                q.append((ny,nx))
ret = 0
for row in dp:
    if 0 in row:
        print(-1)
        exit()
    ret = max(ret, max(row))
print(ret-1)
