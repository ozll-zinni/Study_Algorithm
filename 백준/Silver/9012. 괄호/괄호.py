T = int(input())

for i in range(T):
    s = list(input())
    sum = 0
    
    for j in range(len(s)):
        if s[j] == "(":
            sum += 1
        else:
            sum -= 1
        
        if sum < 0:
            print("NO")
            break
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")