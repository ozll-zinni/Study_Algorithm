n = sorted([int(input()) for _ in range(9)])
diff = sum(n) - 100

for a in n:
    find = False
    for b in n:
        if a+b == diff and a != b:
            find = True
            [print(i) for i in n if i != a and i != b]
            break

    if find:
        break