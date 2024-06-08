N = int(input())
cnt = 0
num = map(int, input().split())

for i in num:
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                cnt += 1
            break

print(cnt)