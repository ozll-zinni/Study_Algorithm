# import sys
n = int(input())
tree = [list(map(int, (input()))) for _ in range(n)] #n x n크기의 리스트로 각 요소는 흰색(0) 또는 파란색(1)임
result = []

def quard_tree(x, y, n): #(x, y) 좌표에서 시작하는 n x n 크기의 부분 종이 탐색
    global result
    color = tree[x][y] # 현재 탐색 중인 부분 종이 첫번재 칸의 색 저장

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != tree[i][j]: #현재 n x n크기의 부분 종이를 탐색하면서 모든 칸이 동일한 색인지 확인, 다른 색이 발견되면 더 작은 부분 종이로 나눔
                result.append("(")
                quard_tree(x, y, n//2) #부분종이의 1사분면
                quard_tree(x, y+n//2, n//2) #부분종이의 2사분면
                quard_tree(x+n//2, y, n//2) #부분종이의 3사분면
                quard_tree(x+n//2, y+n//2, n//2) #부분종이의 4사분면
                result.append(")")
                return
            
    result.append(color)

quard_tree(0,0,n) #초기 (0,0)에서 시작하는 종이에 대해 solution함수 호출 시작
print("".join(map(str,(result))))