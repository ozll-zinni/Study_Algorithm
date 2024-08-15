def f(x, n):
    if x == 1:
        return "m" if n == 1 else "o"

    else: # x> 1일때
        if 2**(x+1) - (x+3) < n < 2**(x+1): # n의 위치가 중간
            return "m" if n == 2 **(x + 1) - (x+2) else "o"
        else: #n의 위치가 왼/오 인경우
            if n >=2 ** (x+1):
                n -= 2**(x+1) -1
            return f(x-1,n)
n = int(input())
x =3
while 2**(x-2) - (x+4) < n:
    x += 1
print(f(x,n))