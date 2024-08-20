'''
** H: 상자수, M: 상자 가로칸 수, N: 상자 세로칸 수
** 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 들어있지 않은 칸

* 3차원 배열을 통해 상,하,좌,우,앞,뒤를 지정해준다
* 1의 값을 가지고 있는 토마토의 위치를 큐에 넣어준다
* 해당 큐를 가지고 BFS를 수행함. -> 3차원 이동이므로 6방향에 대한 이동 경우의 수를 고려해야함.
* 범위를 벗어나지 않으며, (0)익지 않은 토마토가 있을 시 날짜 +1을 해준다 
    => 탐색 횟수를 Tabulation 방식으로 저장해 감으로써 방문 여부를 저장하는 별도의 리스트(visited) 관리없이 최소 탐색 횟수를 구할 수 있게 됌. BFS가 종료되면 이와 같이 저장한 값중 최댓값이 곧 최소 탐색 횟수임
* graph에 BFS의 결과가 반영되었으므로 하나씩 탐색하면서 출력할 결과 값을 결정함
    * 한 곳에서라도 값이 0이 나오면 -1을 출력함
    * 이미 모든 토마토가 익었다면 최댓값은 무조건 1이므로 0을 출력하기 위해 1을 빼주고 출력함
    * 그 외 경우에는 최댓값 -1을 출력함

    가장 큰 값 -1 출력한다. (1일부터 +1을 해가므로 day -1을 해줘야 한다.)
'''

import sys
from collections import deque

m, n, h = map(int, input().split())
graph = [[list(map(int, sys.stdin.readline().split()))for _ in range(n)] for _ in range(h)] #[[[M개의 길이를 가진 리스트]* N개] * H개]
# 움직임 6가지 (상, 하, 좌, 우, 앞, 뒤)
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
queue = deque()

def BFS():
    while queue:
        z, x, y, = queue.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if graph[nz][nx][ny] == 0: #토마토가 익지 않은 경우
                    graph[nz][nx][ny] = graph[z][x][y] + 1 #현재 날짜 + 1
                    queue.append((nz, nx, ny))

#익은 토마토의 위치를 큐에 저장
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))

BFS()

cannot_complete = False
day = 0

#익지 않은 토마토가 있는지 확인. 익지 않은 토마토가 있으면 cannnot_complete를 True로 설정
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                cannot_complete = True
            day = max(day, graph[i][j][k])

if cannot_complete:
    print(-1)
else:
    print(day-1) #날짜는 1일부터 시작하니까 최대 날짜에서 1빼기
