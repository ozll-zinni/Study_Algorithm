def hanoi(one, three, N):
    if N == 1:
        print(one,three)
        return
   
    hanoi(one, 6-one-three, N-1)
    print(one, three)
    hanoi(6-one-three, three, N-1)

N = int(input())
print(2**N-1)
if N <= 20:
    hanoi(1,3,N)