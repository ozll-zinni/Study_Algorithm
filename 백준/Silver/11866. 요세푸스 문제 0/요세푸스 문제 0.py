from collections import deque

n, k = map(int, input().split())
output = [] # 뽑은 수 넣을 리스트
queue = deque()

for i in range(1, n+ 1):
    queue.append(i)

while queue:
    for i in range(k-1):
        queue.append(queue.popleft()) # 큐에서 k번째 뺀 수
    output.append(queue.popleft()) 

print("<", end = "")
print(", ".join(map(str,output)), end="")
print(">", end=" ")
