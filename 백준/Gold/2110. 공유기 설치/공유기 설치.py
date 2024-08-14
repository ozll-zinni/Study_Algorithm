import sys

n, c = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(n)]
houses.sort()

def bi_search(n, c, houses):
    # start = houses[0]
    start = 1
    end = houses[n-1] - houses[0]

    while start <= end:
        distance = (start + end) >> 1

        point = houses[0]
        cnt = 1

        for i in range(1, len(houses)):
            if houses[i] - point >= distance:
                cnt += 1
                point = houses[i]
        if cnt < c:
            end = distance - 1
        elif cnt >= c:
            start = distance + 1
    return end
print(bi_search(n, c, houses))