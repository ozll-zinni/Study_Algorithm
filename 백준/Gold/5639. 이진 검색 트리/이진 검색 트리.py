'''
* 첫번째 값을 root노드로 함
* root값을 비교하여 left와 right 서브트리를 구별함
* 입력 종료 조건이 정해지지 않음 -> sys.setrecursionlimit(10**9)
'''
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

def postorder(start, end):
    if start > end:
        return
    
    mid = end + 1
    for i in range(start + 1, end + 1):
        if preorder[start] < preorder[i]:  # preorder[start]보다 큰 첫 번째 값을 찾음
            mid = i
            break

    postorder(start + 1, mid - 1)  # left 서브트리
    postorder(mid, end)  # right 서브트리
    print(preorder[start])  # 루트 노드 출력

postorder(0, len(preorder) - 1)
