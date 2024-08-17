'''
* 사무실<->집 위치 비교를 위해 (시작점, 끝점)으로 데이터 받기 -> data 리스트
* 끝점(도착점)을 기준으로 오름차순 정렬
* 끝점 - 시작점 <= d인 데이터 찾기
* 각 데이터를 확인하면서 시작점을 heap에 담고, 
돌고 있는 데이터의 끝점을 기준으로 범위 안에 드는 시작점들의 개수를 센다.
'''
import sys
import heapq

# 데이터 입력
n = int(input()) # 기차에 탑승할 사람 수
data = []
for _ in range(n):
    a,b = list(map(int, sys.stdin.readline().split()))
    data.append((max(a,b), min(a,b))) #각 탑승하는 사람의 도착점:max, 출발점:min
data.sort() # 도착점을 기준으로 오름차순 하기 위해 윗 줄에서 max값을 앞에둠

# 거리 입력
d = int(input()) # 거리
heap = [] # 기차 탈 수 있는 사람의 출발점 담을 리스트
max_people = 0 # 지금까지 확인 한 사람 중 기차에 탑승할 수 있는 최대 인원 수를 저장하는 변수

# 탑승 가능한 사람 찾기
for people in data: # 기차 탑승 가능한 사람 찾기
    if people[0] - people[1] <= d: # 현재 사람의 이동거리가 도착점-시작점이 d보다 작거나 같은 경우
        heapq.heappush(heap, people[1]) #heap에 현재 사람의 시작점 추가
    else:
        continue

# 힙에서 유효한 출발점 관리
    while heap:
        start = heap[0] # 제일 빠른 출발점
        if people[0] - start > d: # 제일 빠른 출발점과 각 사람의 출발점 차이가 d보다 날 경우
            heapq.heappop(heap) # start값 제거
        else:
            break

# 탑승 인원 업데이트 
    max_people = max(len(heap), max_people) #현재 힙의 길이: 기차를 탈 수 있는 사람 수를 max_result와 비교

print(max_people)