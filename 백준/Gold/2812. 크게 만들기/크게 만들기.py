n, k = map(int, input().split())
numbers = input()
stack = []

for num in numbers:
    while stack and stack[-1] < num and k >0:
        stack.pop()
        k -= 1
    stack.append(num)
if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))