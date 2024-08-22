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
        row, col = queue.popleft()  # 큐에서 쉘을 하나씩 꺼내 상하좌우로 이동하며 연결된 쉘 탐색
        if total >= k:  # 필요한 쉘의 수가 k 이상이면 True 반환
            return True
        for i in range(4):
            now_r, now_c = row+dx[i], col+dy[i]
            if 0 <= now_r < n and 0 <= now_c < m:  # 새로운 위치가 유효한지 확인
                if mine[now_r][now_c] <= d and not visited[now_r][now_c]:  # 깊이 d 이하이며 방문하지 않은 경우
                    visited[now_r][now_c] = True  # 방문 표시
                    total += 1  # 연결된 쉘 개수 증가
                    queue.append((now_r, now_c))  # 큐에 추가

    return total >= k  # 탐색이 끝난 후 연결된 쉘의 수가 k 이상인지 확인

def main():
    input = sys.stdin.read
    data = input().split()
    
    n, m, k = int(data[0]), int(data[1]), int(data[2])
    mine = []  # 채굴 지역 정보 저장
    index = 3  # 인덱스 시작점은 n, m, k 이후의 첫 번째 데이터부터 시작
    for _ in range(n):
        mine.append(list(map(int, data[index:index + m])))  # 각 행을 리스트로 변환하여 mine에 추가
        index += m  # 다음 행으로 인덱스 이동

    # 이진 탐색을 위한 초기값 설정
    low, high = 0, max(max(row) for row in mine)  # 깊이의 최솟값과 최댓값 설정
    answer = high  # 정답을 최댓값으로 초기화

    # 이진 탐색 수행
    while low <= high:
        mid = (low + high) // 2  # 중간값 계산
        if mining(mine, n, m, k, mid):  # mid 값으로 채굴이 가능한지 확인
            answer = mid  # 가능한 경우 answer를 갱신
            high = mid - 1  # 더 작은 깊이를 찾아보기 위해 범위를 좁힘
        else:
            low = mid + 1  # 더 큰 깊이를 찾아보기 위해 범위를 넓힘
    print(answer)
main()
