C = int(input())

for i in range(C):
    score = list(map(int, input().split()))
    avg = sum(score[1:])/score[0]
    cnt = 0
    for j in score[1:]:
        if j > avg:
            cnt += 1
    per = (cnt/score[0])*100
    print('%.3f'%per+'%')