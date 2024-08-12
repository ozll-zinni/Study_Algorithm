import sys

N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

left , right = 0, N-1
result = [0,0]
min_sum = sys.maxsize

while left < right:
    sum = liquids[left] + liquids[right]

    if abs(sum) < min_sum:
        min_sum = abs(sum)
        result = [liquids[left], liquids[right]]
    
    if sum > 0:
        right -= 1
    else:
        left += 1

print(*result)