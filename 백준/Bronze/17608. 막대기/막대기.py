import sys
input = sys.stdin.readline
n = int(input())
stack= []

for _ in range(n):
    stack.append(int(input()))

count = 0
max = 0

for i in reversed(stack):
    if max < i:
        max = i
        count += 1
print(count)