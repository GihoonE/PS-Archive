import sys
from collections import deque
H,W = map(int,sys.stdin.readline().split())
s = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(H)]
dis = [[-1]*W for _ in range(H)]
dis[0][0] = 1
q = deque([(0,0)])
dx,dy = [1,-1,0,0], [0,0,1,-1]
while len(q) > 0:
    x,y = q.popleft()
    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]
        if 0<=nx<=H-1 and 0<=ny<=W-1 and s[nx][ny] == 1 and dis[nx][ny] == -1:
            dis[nx][ny] = dis[x][y] + 1
            q.append((nx,ny))
print(dis[H-1][W-1])
