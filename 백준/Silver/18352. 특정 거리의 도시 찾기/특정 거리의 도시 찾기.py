import heapq
import sys
INF = float('inf')

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

#간선 연결
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start)) # (거리, 노드) 최소힙은 배열의 첫 번째 값을 기준으로 배열을 정렬.
    distance[start] = 0 # 자기 자신으로 가는 사이클은 없으므로.

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distance[node]: # 비용 최적화 전부터 큰 비용일 경우 고려할 필요 없음.
            continue

        for neighbor in graph[node]: # 최소 비용을 가진 노드를 그리디하게 방문한 경우 연결된 간선 모두 확인
            cost = dist + 1
            if cost < distance[neighbor]: # 여러 경로를 방문해 합쳐진 가중치 W가 더 비용이 적다면 
                distance[neighbor] = cost # 업데이트
                heapq.heappush(heap, (cost, neighbor)) # 최소 비용을 가진 노드와 합쳐진 가중치 추가
dijkstra(x)

flag = 0
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        flag = 1

if flag == 0:
    print(-1)