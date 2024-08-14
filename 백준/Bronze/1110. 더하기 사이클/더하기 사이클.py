n = int(input())
num = n
cnt = 0

while True:
    sum_num = (num//10)+(num%10)
    new_num = ((num%10)*10) + (sum_num%10)
    cnt += 1
    num = new_num
    
    if new_num == n:
        break
print(cnt)