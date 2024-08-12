import sys
n, b = map(int, input().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def matrix(arr1, arr2):
    result = [[0]* n for _ in range(n) ]
    
    for row in range(n):
        for col in range(n):
            s = sum(arr1[row][i] * arr2[i][col] for i in range(n))
            result[row][col] = s % 1000
    return result

def power(n, arr):
    if n == 1:
        return arr
    if n % 2 == 0:
        half = power(n//2, arr)
        return matrix(half, half)
    else:
        return matrix(arr, power(n-1, arr))

for row in power(b, a):
    print(*[r % 1000 for r in row])