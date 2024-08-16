'''
* 중간값을 기준으로 왼/오 나눠서 담기
    ** 중간값보다 작은 것중 가장 큰거 -> 최대 힙 (left)
    ** 중간값보다 큰 것중 가장 작은거 -> 최소 힙 (right)
* 중간값 찾기 위해 왼/오 길이 맞추기
    ** 홀수 : left의 길이가 right보다 하나 더 많아야 함. -> left의 루트가 중간값
    ** 짝수 : left의 루트와 right의 루트의 평균으로 구함.

'''
import sys
import heapq

n = int(input())
left = []  # 중간값보다 작은 것중 가장 큰거 -> 최대 힙
right = [] # 중간값보다 큰 것중 가장 작은거 -> 최소 힙

for i in range(n): # 정수 받기
    num = int(sys.stdin.readline())

    if len(left) == 0 or -left[0] >= num: # 아무것도 없으면 일단 왼쪽, -len[0]: 왼쪽의 루트
        heapq.heappush(left, -num) # 왼쪽이니까 음수로 저장
    else:
        heapq.heappush(right, num)

    if len(left) > len(right) + 1: # 왼쪽의 길이가 오른쪽보다 1큰 경우(최소 2이상 큼)
        temp = -heapq.heappop(left) # 왼쪽의 가장 큰 값을 오른쪽으로 보내서 왼/오 길이 차이가 1 나도록
        heapq.heappush(right, temp)
    elif len(right) > len(left):
        temp = heapq.heappop(right) # 오른쪽의 길이가 왼쪽보다 큰 경우 오른쪽을 왼쪽으로 보내서 왼쪽이 1더 크도록 만듦 -> 왼쪽의 길이가 1차이나야 왼쪽의 root가 무조건 mid 값임
        heapq.heappush(left, -temp)

    print(-left[0]) #왼쪽의 root == mid, 왼쪽은 최대 힙으로 구해서 음수니까 - 붙여줌