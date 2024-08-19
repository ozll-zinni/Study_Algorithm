import sys
n = int(input())
v = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n+1)

for i in range(v):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True  # 정점 v를 방문한 경우 visited에 추가

    for next_node in graph[v]:  # 현재 정점에 연결된 인접 정점들 하나씩 방문
        if not visited[next_node]:  # 아직 방문 안 한 정점이면
            dfs(next_node)  # 해당 정점을 시작점으로 dfs 수행
dfs(1)

print(sum(visited)-1)
