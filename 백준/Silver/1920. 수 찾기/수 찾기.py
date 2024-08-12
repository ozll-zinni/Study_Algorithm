import sys

n = int(input())
n_list = set(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

for target in (m_list):
    print(1 if target in n_list else 0)