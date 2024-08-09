import heapq
import sys

def heapsort(iterable):
    heap = []
    
    for value in iterable:
        heapq.heappush(heap, value)
    
    result = []
    while heap:
        result.append(heapq.heappop(heap))
    
    return result

n = int(sys.stdin.readline().strip())

li = []
for _ in range(n):
    li.append(int(sys.stdin.readline().strip()))

sorted_li = heapsort(li)

for num in sorted_li:
    print(num)
