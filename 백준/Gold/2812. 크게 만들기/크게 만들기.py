n, k = map(int, input().split())
numbers = input().rstrip() # 숫자를 문자열로 입력받음, rstrip()은 없어도 됌
stack = []  # 최적의 숫자를 만들기 위해 사용할 스택

# 주어진 숫자의 각 자리 숫자를 순차적으로 처리
for num in numbers:
    # 스택이 비어있지 않고, 스택의 마지막 숫자가 현재 숫자보다 작고,
    # 아직 제거해야 할 숫자가 남아있는 경우:
    while stack and stack[-1] < num and k > 0:
        stack.pop()  # 스택의 마지막 숫자를 제거
        k -= 1  # 제거할 숫자의 개수를 1 줄임
    stack.append(num)  # 현재 숫자를 스택에 추가

# 만약 제거할 숫자가 남아있는 경우
# -> 스택의 마지막 k개 숫자를 제거하여 숫자를 구성
if k > 0:
    print(''.join(stack[:-k]))
else:
    # 제거할 숫자가 남아있지 않다면, 스택의 모든 숫자를 출력
    print(''.join(stack))