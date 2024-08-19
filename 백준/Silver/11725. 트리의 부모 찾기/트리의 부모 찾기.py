import sys
n = int(input())
sys.setrecursionlimit(10**6)

graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
parent = [0] * (n+1)

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True  # 정점 v를 방문한 경우 visited에 추가

    for next_node in graph[v]:  # 현재 정점에 연결된 인접 정점들 하나씩 방문
        if not visited[next_node]:  # 아직 방문 안 한 정점이면
            parent[next_node] = v
            dfs(next_node)  # 해당 정점을 시작점으로 dfs 수행
dfs(1)

for x in range(2, n+1):
    print(parent[x])
