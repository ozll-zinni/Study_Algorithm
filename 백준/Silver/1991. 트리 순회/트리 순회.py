import sys

n = int(sys.stdin.readline())
tree = {}

for n in range(n):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]

    
# 전위 순회
def preorder(root):
    if root != '.':
        print(root, end='')  # 루트 노드 출력
        preorder(tree[root][0])  # 왼쪽 서브트리 순회
        preorder(tree[root][1])  # 오른쪽 서브트리 순회

# 중위 순회 
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # 왼쪽 서브트리 순회
        print(root, end='')  # 루트 노드 출력
        inorder(tree[root][1])  # 오른쪽 서브트리 순회

# 후위 순회
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # 왼쪽 서브트리 순회
        postorder(tree[root][1])  # 오른쪽 서브트리 순회
        print(root, end='')  # 루트 노드 출력

preorder('A')
print()

inorder('A')
print()

postorder('A')
print()