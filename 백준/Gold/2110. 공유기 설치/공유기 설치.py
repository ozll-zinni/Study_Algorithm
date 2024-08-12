import sys

N, C = map(int, input().split())
houses =  [int(sys.stdin.readline()) for _ in range(N)]
houses.sort()

left, right = 1, houses[-1] - houses[0]
result = 0
while left <= right:
    mid = (left + right) //2

    prev_house = houses[0]
    count = 1
    
    for i in range(1, len(houses)):
        if houses[i] - prev_house >= mid:
            prev_house = houses[i]
            count += 1
    
    if count >= C:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)