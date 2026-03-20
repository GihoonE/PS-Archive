import sys
import heapq
input = sys.stdin.readline
T = int(input())
def dijkstra(start, edge, N):
    h = []
    visited = [float('inf')]*(N+1)
    visited[start] = 0
    heapq.heappush(h,(0,start))
    while h:
        cur_dist, cur_node = heapq.heappop(h)
        if cur_dist > visited[cur_node]:
            continue
        for dist, next_node in edge[cur_node]:
            if cur_dist + dist < visited[next_node]:
                visited[next_node] = cur_dist + dist
                heapq.heappush(h,(visited[next_node],next_node))
    return visited
 
for o in range(T):
    # 교차로, 도로, 목적지 후보 수
    n,m,t = map(int,input().split())
    # 출발지, g, h 노드들
    s,g,h = map(int,input().split())
    gh_dist = 0
    edge = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int,input().split())
        edge[a].append((d,b))
        edge[b].append((d,a))
        if (a == g and b == h) or (a == h and b == g):
            gh_dist = d
    ans = []
    # from s
    s_rrr = dijkstra(s,edge,n)
    # from h
    h_rrr = dijkstra(h,edge,n)
    # from g
    g_rrr = dijkstra(g,edge,n)
    for _ in range(t):
        dest = int(input())
        cand1 = s_rrr[g]+gh_dist+h_rrr[dest]
        cand2 = s_rrr[h]+gh_dist+g_rrr[dest]
        if s_rrr[dest] == cand1 or s_rrr[dest] == cand2:
            if s_rrr[dest] != float('inf'):
                ans.append(dest)
    print(' '.join(map(str, sorted(ans))))

