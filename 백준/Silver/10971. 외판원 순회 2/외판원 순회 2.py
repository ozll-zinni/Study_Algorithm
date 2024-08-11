import sys
n = int(input())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
min_cost = sys.maxsize

def get_cost(cost, visited, cur_idx, first_idx):
    global min_cost

    if all(visited):
        if costs[cur_idx][first_idx] != 0:
            min_cost = min(min_cost, cost+costs[cur_idx][first_idx])
        return
    
    for i in range(n):
        if not visited[i] and costs[cur_idx][i] != 0:
            visited[i] = True
            get_cost(cost+ costs[cur_idx][i], visited, i, first_idx)
            visited[i]=False

for i in range(n):
    visited = [False]*n
    visited[i] = True
    get_cost(0, visited, i, i)
print(min_cost)