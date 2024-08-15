import sys
input = sys.stdin.readline

score = 0
mushroom = []

for _ in range(10):
    mushroom.append(int(input()))

for i in mushroom:
    score += i
    if score >= 100:
        if score - 100 > 100 - (score - i):
            score -= i
            break
print(score)