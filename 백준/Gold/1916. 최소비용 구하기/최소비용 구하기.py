'''
1. 최소비용을 기준으로 각 노드의 최소 비용 저장
2. 방문하지 않은 노드 중 가장 비용이 적은 노드 선택
3. 해당 노드를 거쳐 특정한 노드로 가는 경우를 고려하여 최소 비용 계산
'''

import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
start, end = map(int, input().split())

def dijkstra(graph, start):
    cost = [1e9 for _ in range(n+1)]
    cost[start] = 0 #시작 노드의 거리는 0 (자기자신)
    heap = []
    heapq.heappush(heap, [0, start]) #시작 노드부터 탐색

    while heap:
        cur_cost, cur_v = heapq.heappop(heap)
        if cost[cur_v] < cur_cost: #기존 최단 거리보다 멀면 무시
            continue

        # 노드와 연결된 인접노드 탐색
        for next_node, next_cost in graph[cur_v]:
            sum_cost = cur_cost + next_cost #인접 노드까지 거리
            if sum_cost < cost[next_node]: # 기존 거리보다 짧으면
                cost[next_node] = sum_cost
                heapq.heappush(heap, [sum_cost, next_node]) #다음 인접 거리 계산하기 우해 큐에 삽입
    return(cost)

dist_start = dijkstra(graph, start)
print(dist_start[end])
