import sys

m, n, l = map(int, input().split())
stations = list(map(int, input().split()))
stations.sort()

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return right

count = 0
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    idx = binary_search(stations, x)

    # 현재 위치에서의 거리 계산
    dist = abs(x - stations[idx]) + y

    # 오른쪽 인덱스의 거리 계산
    if idx < m - 1:
        dist_right = abs(x - stations[idx + 1]) + y
        dist = min(dist, dist_right)

    # 사정거리 L과 비교
    if dist <= l:
        count += 1

print(count)
