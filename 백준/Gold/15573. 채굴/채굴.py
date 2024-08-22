import sys
from collections import deque

input = sys.stdin.readline

def mining(mine, n, m, k, d): #채굴 지역mine, 행/열 n,m, 필요한 쉘의 수k, 길이d
    total = 0 #연결된 쉘개수
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[False] * m for _ in range(n)]
    queue = deque()

    #경계 설정하기 위해 첫번째 행과 마지막 열 기준으로 깊이 d 이하인 쉘을 찾아 큐에 추가하고 방문 표시
    for i in range(m): #첫번째 행의 모든 열 순회하며 깊이 d이하인 쉘 큐에 추가
        if mine[0][i] <= d:
            queue.append((0, i))
            visited[0][i] = True
            total += 1
    for i in range(1, n): #첫번째 열과 마지막 열의 쉘을 순회하면서 깊이 d이하인 쉘을 큐에 추가
        if mine[i][0] <= d:
            queue.append((i, 0))
            visited[i][0] = True
            total += 1
        if mine[i][m-1] <= d:
            queue.append((i, m-1))
            visited[i][m-1] = True
            total += 1

    while queue: #큐에서 쉘을 하나씩 꺼나고 상하좌우로 이동하며 연결된 쉘 탐색-> BFS
        row, col = queue.popleft()
        if total >= k:
            return True
        for i in range(4):
            now_r, now_c = row+dx[i], col+dy[i]
            if 0 <= now_r < n and 0<= now_c < m:
                if mine[now_r][now_c] <= d and not visited[now_r][now_c]: #새로운 위치가 유효하고, 깊이 d이하이며 방문하지 않은 경우
                    visited[now_r][now_c] = True #해당 쉘을 큐에 추가하고 방문 표시
                    total += 1
                    queue.append((now_r, now_c))
    return total >= k #탐색 끝나고 연결된 쉘의 수가 k이상인지 확인

def main():
    input = sys.stdin.read
    data = input().split()
    
    n, m, k = int(data[0]), int(data[1]), int(data[2])
    mine = []
    index = 3
    for _ in range(n):
        mine.append(list(map(int, data[index:index + m])))
        index += m 

    low, high = 0, max(max(row) for row in mine)
    answer = high

    while low <= high:
        mid = (low + high) // 2
        if mining(mine, n, m, k, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    print(answer)
main()
