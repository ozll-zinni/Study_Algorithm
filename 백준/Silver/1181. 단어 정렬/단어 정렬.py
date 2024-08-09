import sys
import heapq

n = int(sys.stdin.readline())
res = []

for i in range(n):
    a = sys.stdin.readline().rstrip()
    heapq.heappush(res, (len(a), a))

res = list(set(res))
res.sort(key=lambda x:(x[0], x[1]))

for r in res:
    print(r[1])