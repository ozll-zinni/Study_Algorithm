def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())

for _ in range(n):
    num = int(input())

    a, b = num//2, num//2
    
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a,b)
            break
        a -= 1
        b += 1
            