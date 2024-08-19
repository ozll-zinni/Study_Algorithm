'''
* 인접한 노드끼리 서로 다른 집합/색에 들어가게 만들 수 있으면 이분 그래프임
* 인접 노드 탐색시
    1. 현재 집합고 다른 집합으로 표시하고, 인접 노드 중에서 현재 노드 집합과 같은 집합에 속한 노드를 만나면 no출력
    2. 깊이로 쭉 탐색하기 위해 dfs를 활용한다. <형제노드와 색을 출력하는 bfs로 구현하는건 왜 안될까?>

* 현재 노드 집합과 인접한 노드의 집합 저장
    1. 0: 방문x, 1: 집합A, 2:집합B
    2. 초기 dfs 인자를 group에 1을 담아 dfs를 호출하고, 인접 노드로 타고 가면서 dfs를 호출할 때는 -group을 전달해서 현재 노드와 인접 노드의 group을 다른 값으로 넣어준다.
        -> 현재 노드가 1이면 인접노드는 -1이 되고, 인접 노드의 인접노드는 다시 1로 나올 것임

* 인접 노드끼리 다른 집합에 속하는지 확인한다
    1. 이미 방문한 노드라면(if visited[v] == 0:가 아니면) 현재 노드의 groupㅘ 인접 노드의 group값이 다른지 확인
    2-1. 현재 노드의 group과 인접 노드의 group이 다르면 이분 그래프
    2-2. 현재 노드의 group과 인접 노드의 group이 같으면 false 출력

* 모든 노드에 대해 DFS 수행함
    1. 입력값을 받아서 방문하지 않은 모든 노드에 DFS를 호출함
    2. DFS가 False를 리턴하면 바로 멈추고 출력
'''

import sys
sys.setrecursionlimit(10**9)
k = int(input())


def DFS(start, visited, graph, group):
    visited[start] = group # 현재 노드의 그룹 지정

    # 인접노드 탐색
    for next_node in graph[start]:
        if visited[next_node] == 0: #아직 방문하지 않은 노드라면
            result = DFS(next_node, visited, graph, -group) # -group을 통해 현재 노드의 집합과 다른 집합으로 함
            if not result: #그룹이 겹쳐서 False를 리턴한 경우 탐색을 멈추고 호출된 함수들에 대해서도 False 리턴해야 함 -> DFS를 재귀적으로 호출할 때 리턴값을 받아서 False인 경우에도 리턴함
                return False
        elif visited[next_node] == group: # 이미 방문한 곳 중에서 노드가 현재 그룹과 같으면 이분 그래프가 아님
            return False
    return True

# 테스트 케이스 처리
for _ in range(k):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V+1):
        if visited[i] == 0:
            result = (DFS(i, visited, graph, 1))
            if not result:
                break
    print("YES") if result else print("NO")

