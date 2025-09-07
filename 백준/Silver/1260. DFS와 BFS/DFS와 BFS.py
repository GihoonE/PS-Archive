
import sys
V,E,S = map(int,sys.stdin.readline().split())
dp = [[0] for _ in range(1001)]

for _ in range(E):
    a,b = map(int,sys.stdin.readline().split())
    dp[a].append(b)
    dp[b].append(a)

stack = [S]
dfs = []
while len(stack) > 0:
    cur = stack.pop()
    if dp[cur][0] == 0:
        dfs.append(cur)
        dp[cur][0] = -1
        arr = sorted(dp[cur])
        for i in range(len(dp[cur])-1,0,-1):
            stack.append(arr[i])
print(" ".join(list(map(str,dfs))))

from collections import deque
q = deque()
q.append(S)
bfs = []
while len(q) > 0:
    cur = q.popleft()
    if dp[cur][0] == - 1:
        bfs.append(cur)
        dp[cur][0] = 0
        arr = sorted(dp[cur])
        for i in range(1,len(dp[cur])):
            q.append(arr[i])
print(" ".join(list(map(str,bfs))))