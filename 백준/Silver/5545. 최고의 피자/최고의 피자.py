n = int(input())
a, b = map(int, input().split())
c = int(input())
topping = [int(input()) for _ in range(n)]
topping.sort(reverse=True)
result = c // a
d = c
price = a
for k in range(n):
    price += b
    d += topping[k]
    result = max(result, d // price)
print(result)