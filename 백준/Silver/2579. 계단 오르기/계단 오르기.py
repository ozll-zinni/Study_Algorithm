N=int(input())

satir=[0]
dp = [0 for _ in range(N+1)]

for _ in range(N):
    satir.append(int(input()))


if N==1:
    print(satir[1])

else:
    dp[1] = satir[1]
    dp[2] = satir[1] + satir[2]

    for k in range(3,N+1):
        dp[k] = max(dp[k-3] + satir[k-1], dp[k-2]) + satir[k]

    print(dp[N])