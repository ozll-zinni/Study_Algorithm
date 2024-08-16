import heapq as hp
import sys

n = int(input())
max_heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        hp.heappush(max_heap, -x) #파이썬 heapq는 최소 힙이라 음수로 변경
    else:
        if not max_heap:
            print(0)
        else:
            print(-hp.heappop(max_heap)) #음수로 저장되어 있어, 다시 -붙여줌