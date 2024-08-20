'''
* 0이면 부수고, 부순횟수 카운트하기. 1이면 그냥 이동
* 힙에다 부순 횟수 저장해서 push, pop하기
'''
import sys
import heapq

n = int(input())
# 2차원 리스트 만들기
graph = [list(map(int, input().strip())) for _ in range(n)]
distance = [[sys.maxsize] * n for _ in range(n)]         
# 움직임 4가지 (상, 하, 좌, 우)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 0, 0))  # (부순 횟수, x, y)
    distance[0][0] = 0

    while heap:
        count, x, y = heapq.heappop(heap)  # 부순 횟수가 적은 경로를 우선으로 하기 위해 (부순 횟수, x, y) 순서로 수정
        
        # 현재 위치가 이미 더 짧은 거리로 방문된 경우 무시
        if distance[x][y] < count:
            print(count)
            continue

        for i in range(4):  
            next_x, next_y = x + dx[i], y + dy[i]
            
            # 좌표에서 벗어나지 않는지 확인
            if 0 <= next_x < n and 0 <= next_y < n:
                # 새 비용 계산
                if graph[next_x][next_y] == 1:
                    new_cost = count  # 흰 방으로 이동 (부수지 않음)
                else:
                    new_cost = count + 1  # 장애물 칸으로 이동

                # 새로운 비용이 더 작은 경우 업데이트
                if new_cost < distance[next_x][next_y]:
                    distance[next_x][next_y] = new_cost
                    heapq.heappush(heap, (new_cost, next_x, next_y))

dijkstra()

# 목표 지점(n-1, n-1)까지의 최단 경로 출력
if distance[n-1][n-1] == sys.maxsize:
    print(-1)  # 도달할 수 없는 경우
else:
    print(distance[n-1][n-1])

