from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
campus = [] #캠퍼스 정보 담기
ix, iy = 0, 0 #시작 위치 초기화
meet = 0 #만난 사람 초기화

n, m = map(int, input().split())

for i in range(n):
    campus.append(list(input()))
    for j in range(m):
        if campus[i][j] == 'I': #I 위치로 시작 위치 찾기
            ix, iy = i, j

visited = [[0] * m for _ in range(n)] # 방문 정보 담을 리스트

deq = deque()
deq.append([ix, iy]) # 최초 시작 위치 insert

while deq: # 큐가 빌 때까지
    x, y = deq.popleft()
    for i in range(4):  # 상하좌우 탐색
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0: # 방문 안했으면 
            visited[nx][ny] = 1 # 방문 표시
            if campus[nx][ny] == 'O':  # 빈 공간 이면 
                deq.append([nx, ny])
            elif campus[nx][ny] == 'P':  # 사람 이면
                deq.append([nx, ny])
                meet += 1 # 만난 사람 수 증가

print('TT' if meet == 0 else meet) # 정답 출력