import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())

dp = [[0] * n for _ in range(n)]
        
for i in range(n):
    for start in range(n - i):
        end = start + i
        
        # 시작점과 끝점이 같다면
        if start == end: #숫자가 1개일 경우 무조건 1
            dp[start][end] = 1
        # 시작점의 글자와 끝점의 글자가 같다면
        elif numbers[start] == numbers[end]:
            if start + 1 == end: #시작과 끝 글자가 같고, 2글자 인경우
                dp[start][end] = 1 # 무조건 펠린드롬
            elif dp[start+1][end-1] == 1: #글자가 3개 이상인 경우이고, 시작값과 끝 값은 위에서 판별함 -> 가운데 문자열이 펠린드롬이면
                dp[start][end] = 1
            

#정답출력하기
for question in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])