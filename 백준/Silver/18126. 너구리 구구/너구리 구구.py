import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    visited[v] = 1
    for i in range(len(adjList[v])):
        w = adjList[v][i][0]
        if not visited[w]:
            dist[w] = adjList[v][i][1] + dist[v]
            dfs(w)

n = int(sys.stdin.readline())
visited = [0 for i in range(n+1)]
adjList = [[] for i in range(n+1)]
dist = [0 for i in range(n+1)]
for i in range(1, n):
    a, b, c = map(int, sys.stdin.readline().split())
    adjList[a].append([b, c])
    adjList[b].append([a, c])

dfs(1)
print(max(dist))