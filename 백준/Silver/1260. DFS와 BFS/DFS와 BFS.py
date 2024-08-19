from collections import deque
import sys
n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 작은 번호부터 방문하도록 각 정점의 인접 리스트 정렬
for g in graph:
    g.sort()


def dfs(v):
    # 현재 정점 v를 방문했음을 표시하고 결과 리스트에 추가
    dfs_visited[v] = True
    dfs_result.append(v)

    # 현재 정점에 연결된 인접 정점들을 하나씩 방문
    for next_node in graph[v]:
        if not dfs_visited[next_node]:  # 아직 방문하지 않은 정점인 경우
            dfs(next_node)  # 해당 정점을 시작점으로 다시 DFS 수행


def bfs(start):
    # 방문한 정점을 체크하기 위한 리스트
    bfs_visited = [False] * (n+1)
    # 시작점 방문 체크
    bfs_visited[start] = True
    bfs_result = []

    # BFS를 위한 큐 생성, 시작점을 큐에 추가
    queue = deque([start])
    while queue:
        # 큐의 맨 앞에 있는 정점을 꺼내서 방문
        visit = queue.popleft()
        bfs_result.append(visit)

        # 현재 정점에 연결된 인접 정점들을 하나씩 방문
        for next_node in graph[visit]:
            if not bfs_visited[next_node]:  # 아직 방문하지 않은 정점인 경우
                bfs_visited[next_node] = True  # 해당 정점을 방문 체크하고 큐에 추가
                queue.append(next_node)

    return bfs_result


dfs_visited = [False] * (n+1)
dfs_result = []
dfs(start)

bfs_result = bfs(start)

print(*dfs_result)
print(*bfs_result)