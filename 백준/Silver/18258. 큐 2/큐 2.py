import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
queue = deque()  # deque를 사용하여 효율적인 큐 연산을 처리

for _ in range(n):
    s = input().split()
    
    if s[0] == 'push':
        queue.append(s[1])  # 큐의 뒤에 요소를 추가
    
    elif s[0] == 'pop':
        if queue:
            print(queue.popleft())  # 큐의 앞에서 요소를 제거하고 출력
        else:
            print(-1)  # 큐가 비어있다면 -1 출력
    
    elif s[0] == 'size':
        print(len(queue))  # 큐에 있는 요소의 개수를 출력
    
    elif s[0] == 'empty':
        print(1 if not queue else 0)  # 큐가 비어있다면 1, 아니면 0 출력
    
    elif s[0] == 'front':
        if queue:
            print(queue[0])  # 큐의 가장 앞에 있는 요소를 출력
        else:
            print(-1)  # 큐가 비어있다면 -1 출력
    
    elif s[0] == 'back':
        if queue:
            print(queue[-1])  # 큐의 가장 뒤에 있는 요소를 출력
        else:
            print(-1)  # 큐가 비어있다면 -1 출력
