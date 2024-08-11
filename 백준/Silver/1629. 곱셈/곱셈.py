A, B, C = map(int, input().split())

def modular_exponentiation(A, B, C):
    result = 1
    A = A % C
    while B > 0:
        if B % 2 == 1:
            result = (result * A) % C
        
        B = B // 2
        A = (A * A) % C
    
    return result

result = modular_exponentiation(A, B, C)
print(result)