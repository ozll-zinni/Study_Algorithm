n, m = map(int, input().split())
trees = list(map(int, input().split()))

def binary_search(trees, target):
    left, right = 0, max(trees)

    while left <= right:
        mid = (left+right) //2
        total = 0
        for h in trees:
            if h > mid:
                total += h - mid
        
        if total < target:
            right = mid -1
        else:
            left = mid + 1
    return right

print(binary_search(trees, m))
