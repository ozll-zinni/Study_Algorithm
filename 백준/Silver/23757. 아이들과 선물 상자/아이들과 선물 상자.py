import sys
import heapq
n,m = map(int,input().split())
c = list(map(int,sys.stdin.readline().split()))
w = list(map(int,sys.stdin.readline().split()))
hq = []
for i in c:
	heapq.heappush(hq,-i)

for i in w:
	mx = -heapq.heappop(hq)
	if mx < i:
		print(0)
		exit()
	heapq.heappush(hq,-(mx-i))
	
print(1)