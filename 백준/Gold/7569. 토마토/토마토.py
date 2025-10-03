import sys
from collections import deque
N,M,H = map(int,sys.stdin.readline().strip().split())
dp = []
q = deque()
for h in range(H):
    floor = []
    for i in range(M):
        row = list(map(int,sys.stdin.readline().split()))
        floor.append(row)
        for j in range(N):
            if row[j] == 1:
                q.append((i,j,h))
    dp.append(floor)

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dh = [0,0,0,0,-1,1]
while q:
    cy,cx,ch = q.popleft()
    for i in range(6):
        nh,ny,nx = ch+dh[i],cy+dy[i],cx+dx[i]
        if 0 <= ny <= M-1 and 0 <= nx <= N-1 and 0 <= nh <= H-1:
            if dp[nh][ny][nx] == 0:
                dp[nh][ny][nx] = dp[ch][cy][cx] + 1
                q.append((ny,nx,nh))
ret = 0
for f in dp:
    for row in f:
        if 0 in row:
            print(-1)
            exit()
        ret = max(ret, max(row))
print(ret-1)