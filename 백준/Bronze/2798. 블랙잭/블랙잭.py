n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            current_sum = arr[i] + arr[j] + arr[k]
            if current_sum <= m:
                result = max(result, current_sum)

print(result)
