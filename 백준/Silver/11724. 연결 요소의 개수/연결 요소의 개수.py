'''
1. 연결된 뭉텅이가 몇개인가?
2. dfs를 이용하면 연결된 요소를 모두 방문 -> 한 요소에 대한 탐색이 종료되고, 새로 탐색 시작 = 연결 끊김
3. 탐색이 끊기고 새롭게 탐색 시작되는 횟수 세기
'''

import sys
sys.setrecursionlimit(10**6)

n,m = map(int, input().split())

def dfs(start):
    visited[start] = True
    for next in graph[start]:
        if not visited[next]:
            dfs(next)

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(m): # 간선 정보 넣기
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)