import sys
from collections import deque
V,E,S = map(int,sys.stdin.readline().strip().split())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    a,b = map(int,sys.stdin.readline().strip().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [False]*(V+1)
stack = [S]
ind = 1
while stack:
    current_node = stack.pop()
    if visited[current_node] == 0:
        visited[current_node] = ind
        ind += 1
        adjs = sorted(arr[current_node],reverse=True)
        # print(f'{current_node} adjs: {adjs}')
        for next_node in adjs:
            stack.append(next_node)

for i in range(1,len(visited)):
    if visited[i]:
        print(visited[i])
    else:
        print(0)