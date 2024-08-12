import sys

n, k = map(int, input().split())
levels = [int(sys.stdin.readline()) for _ in range(n)]

levels.sort()

left, right = levels[0], levels[-1] +k

def find_diff(mid):
    diff = 0
    for level in levels:
        if level < mid:
            diff += mid - level
        else:
            break
    return diff

while left <= right:
    mid = (left + right) // 2
    diff = find_diff(mid)
    if diff <= k:
        left = mid + 1
    else:
        right = mid - 1

print(right)