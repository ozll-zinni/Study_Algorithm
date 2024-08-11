N, r, c = map(int, input().split())

def recur(N, row, col):
    if N == 0:
        return 0
    cur_count = 2*(row%2) + (col%2)
    return 4*recur(N-1, row//2, col//2) + cur_count

print(recur(N, r, c))