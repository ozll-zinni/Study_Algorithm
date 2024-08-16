def turn(dir, c):  # 회전
    if c == "L":
        return (dir + 3) % 4  # 왼쪽으로 회전
    else:
        return (dir + 1) % 4  # 오른쪽으로 회전

def print_map(map):
    for i in range(len(map)):
        print(map[i])

def solution():
    n = int(input())
    maps = [[0] * (n + 1) for _ in range(n + 1)]

    k = int(input())
    for _ in range(k):
        x, y = map(int, input().split())
        maps[x][y] = 2  # 사과 위치 설정

    l = int(input())
    turns = []  # 방향 전환 정보를 저장할 리스트
    for _ in range(l):
        x, c = input().split()
        turns.append([int(x), c])

    x, y = 1, 1  # 뱀의 시작 위치
    maps[x][y] = 1  # 뱀의 몸통 위치 설정

    dx = [0, 1, 0, -1]  # 오른쪽, 아래쪽, 왼쪽, 위쪽 이동
    dy = [1, 0, -1, 0]

    direction = 0  # 초기 방향 (오른쪽)
    time = 0
    turn_index = 0

    snake_index = [[x, y]]  # 뱀의 몸통 위치를 저장할 리스트

    while True:
        # 다음 위치 계산
        x += dx[direction]
        y += dy[direction]
        time += 1

        # 게임 종료 조건
        if x <= n and y <= n and x >= 1 and y >= 1 and maps[x][y] != 1:
            if maps[x][y] != 2:  # 사과가 아닌 경우
                px, py = snake_index.pop(0)  # 꼬리 위치 제거
                maps[px][py] = 0  # 맵에서 꼬리 제거
            maps[x][y] = 1  # 새로운 머리 위치 설정
            snake_index.append([x, y])  # 뱀의 몸통에 새로운 머리 추가

            # 방향 전환 체크
            if turn_index < len(turns) and turns[turn_index][0] == time:
                direction = turn(direction, turns[turn_index][1])  # 방향 전환
                turn_index += 1
        else:
            break  # 벽에 부딪히거나 자기 자신과 충돌

    return time

print(solution())
