from collections import deque
import sys
n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph: # 작은 번호부터 방문하기 위해 각 정점의 인접 리스트 정렬
    g.sort()  # 여기에 괄호를 추가해야 리스트가 정렬됩니다.

def dfs(v):
    dfs_visited[v] = True  # 정점 v를 방문한 경우 visited에 추가
    dfs_result.append(v)

    for next_node in graph[v]:  # 현재 정점에 연결된 인접 정점들 하나씩 방문
        if not dfs_visited[next_node]:  # 아직 방문 안 한 정점이면
            dfs(next_node)  # 해당 정점을 시작점으로 dfs 수행

def bfs(start):
    bfs_visited = [False] * (n+1)  # 방문한 정점 체크하기 위한 리스트
    bfs_result = []

    bfs_visited[start] = True  # 시작점 방문 체크    
    queue = deque([start])  # bfs를 위한 큐 생성, 시작점을 큐에 추가

    while queue:
        visit = queue.popleft()  # 큐의 맨 앞에 있는 정점을 꺼내서 방문
        bfs_result.append(visit)

        for next_node in graph[visit]:  # 현재 정점에 연결된 인접 정점들을 하나씩 방문
            if not bfs_visited[next_node]:  # 아직 방문 안 한 정점이면
                bfs_visited[next_node] = True  # 해당 정점을 방문하고 큐에 추가
                queue.append(next_node)

    return bfs_result

dfs_visited = [False] * (n+1)
dfs_result = []
dfs(start)

bfs_result = bfs(start)

print(*dfs_result)
print(*bfs_result)
