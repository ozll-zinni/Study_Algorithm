n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
num = []
answer = 0

def dfs(depth):
    if depth == 3:
        global answer
        for i in range(n):
            strike, ball = 0, 0
            for j in range(3):
                target = str(graph[i][0])
                if int(target[j]) == num[j]:
                    strike += 1
                elif int(target[j]) in num:
                    ball += 1
            if strike != graph[i][1] or ball != graph[i][2]:
                return
        answer += 1
        return
    
    for i in range(1, 10):
        if i not in num:
            num.append(i)
            dfs(depth + 1)
            num.pop()
dfs(0)
print(answer)