n = int(input())

for i in range(n):
    a = input()
    score = 0
    sumscore = 0
    for j in a:
        if j == 'O':
            score += 1
        else:
            score = 0
        sumscore += score
    print(sumscore)