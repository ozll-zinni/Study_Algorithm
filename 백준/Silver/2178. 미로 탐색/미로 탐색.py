'''
* 최단 경로 이므로 bfs를 활용한다
* 시작점에서부터 탐색을 시작하며, 각 칸마다의 거리를2
'''
from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

# 2차원 리스트 만들기
graph = [list(map(int, ''.join(sys.stdin.readline().strip()))) for _ in range(N)]

queue = deque([(0, 0)])  # 시작점을 튜플로 큐에 추가
         
# 움직임 4가지 (상, 하, 좌, 우)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        next_x, next_y = x + dx[i], y + dy[i]
        
        # 좌표에서 벗어나지 않는지 확인하고, 이동 가능한 칸인지 확인
        if 0 <= next_x < N and 0 <= next_y < M and graph[next_x][next_y] == 1:
            # 큐에 다음 위치 추가하고 이동한 거리 기록
            queue.append((next_x, next_y))
            graph[next_x][next_y] = graph[x][y] + 1

# 목표 지점(N-1, M-1)까지의 최단 경로 출력
print(graph[N-1][M-1])
