import sys
from collections import deque
V = int(sys.stdin.readline().strip())
E = int(sys.stdin.readline().strip())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    a,b = map(int,sys.stdin.readline().strip().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [False]*(V+1)
deque = deque()
deque.append(1)
ind = 1
while deque:
    current_node = deque.popleft()
    if visited[current_node] == 0:
        visited[current_node] = ind
        ind += 1
        adjs = sorted(arr[current_node])
        for nn in adjs:
            deque.append(nn)
c = 0
for i in range(1,len(visited)):
    if visited[i]:
        c += 1
print(c-1)