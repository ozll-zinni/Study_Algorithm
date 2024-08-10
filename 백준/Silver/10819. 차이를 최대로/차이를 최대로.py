n = int(input())
a = list(map(int, input().split()))
max_value = 0

def get_sum(permu):
    return sum(abs(permu[i]-permu[i+1]) for i in range(n-1))

def recur(permu,visited):
    global max_value
    if len(permu) == n:
        max_value = max(max_value, get_sum(permu))

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            recur(permu + [a[i]], visited)
            visited[i] = False
    
visited = [False] * n
recur([], visited)

print(max_value)