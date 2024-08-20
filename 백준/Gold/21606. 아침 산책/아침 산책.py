import sys
sys.setrecursionlimit(10**6)

N = int(input())
inside = '0' + input()  # 각 노드가 실내(1)인지 실외(0)인지 저장한 문자열
# 노드 번호를 index로 접근하기 위해 앞에 0 추가

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
total = 0 # 경로의 개수를 저장할 변수


for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

    # 두 정점 모두 실내이면 경로의 수 2 증가
    if inside[a] == "1" and inside[b] == "1":
        total += 2


def DFS(start):
    visited[start] = True # 방문 처리
    inside_count = 0 # 현재 노드와 인접한 실내 노드 개수를 저장할 변수
    for v in graph[start]:
        # 인접한 노드가 실내라면
        if inside[v] == '1': 
            inside_count += 1 # 실내 노드 개수 증가

        # 인접한 노드가 실외라면
        elif not visited[v] and inside[i] == "0": # 그 노드에서부터 탐색하여 실내 노드 개수 증가
            inside_count += DFS(v)
    return inside_count # 실내 노드 개수 반환


for i in range(1, N+1):
    if inside[i] == '0' and not visited[i]: # 시작이 실외일 때만 탐색
        result = DFS(i) # DFS를 통해 인접한 실내 노드 개수를 계산
        total += (result) * (result - 1) # 경로의 개수 추가

print(total)