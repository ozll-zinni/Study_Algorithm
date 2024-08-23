s1 = [0] + list(input())
s2 = [0] + list(input())

len_1 = len(s1)
len_2 = len(s2)

lcs = [['' for _ in range(len_1)] for _ in range(len_2)]

for i in range(1, len_2):
    for j in range(1, len_1):
        if s1[j] == s2[i]:
            lcs[i][j] = lcs[i-1][j-1] + s1[j]
        else:
            if len(lcs[i][j-1]) > len(lcs[i-1][j]):
                lcs[i][j] = lcs[i][j-1]
            else:
                lcs[i][j] = lcs[i-1][j]

answer = len(lcs[-1][-1])
print(answer)
if answer != 0:
    print(lcs[-1][-1])
