import sys
input = sys.stdin.readline

testcase = int(input())
for t in range(testcase):
    n = int(input()) #동전의 종류(가지) 수
    coins = list(map(int, input().split())) #동전의 종류
    m = int(input()) #만들 금액

    dp = [0] * (m+1) # dp[n] : n 금액에 대한 동전 교환 방법의 가지 수 
    dp[0] = 1 # 0원은 아무 동전도 사용하지 않는 경우가 하나 있으므로 1으로 설정

    for coin in coins:
        for i in range(coin, m+1):
            dp[i] += dp[i - coin]
    print(dp[m])