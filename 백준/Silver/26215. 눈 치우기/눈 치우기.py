from sys import stdin
import heapq
n = int(stdin.readline())
snows = list(map(int, stdin.readline().split()))
cnt = 0
heap = []
for snow in snows:
    if snow > 1440:
        print(-1)
        exit(0)
    else:
        heapq.heappush(heap, -snow)

while len(heap) > 1:
    max_val = -heapq.heappop(heap)
    sec_val = -heapq.heappop(heap) if heap else 0

    heapq.heappush(heap, -(max_val - sec_val))
    cnt += sec_val

cnt += -heapq.heappop(heap) if heap else 0
print(-1 if cnt > 1440 else cnt)