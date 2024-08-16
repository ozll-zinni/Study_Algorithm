'''
* 가장 작은 묶음을 두 개씩 찾아서 더해주는 것이 가장 적게 비교하는 방법
* 가장 작은 두 묶음을 구해서 더하고, 새로 만들어진 묶음을 다시 큐에 넣는다.
* 큐에서 또다시 작은 두 묶음을 구하고 더하는 것을 반복한다.
'''

import sys
import heapq

n = int(input())
heap = []
for i in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

total_sum = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    sum = a + b

    total_sum += sum
    heapq.heappush(heap, sum)
print(total_sum)
