# 각 버섯의 점수가 담긴 리스트 준비
mushroom_list = [None]*10

for i in range(10):
    mushroom_list[i] = int(input())

# 누적 점수 계산 함수 : return 값 = 최대 점수
def calc_score(arr):
    # 리턴할 최대 점수를 저장하기 위한 변수
    answer = 0
    # 누적 점수를 계산하기 위한 변수
    sum = 0
    # 100과의 차이를 저장하기 위한 변수
    diff = float('inf')

    # 10번만 계산하면 되기 때문에 브루트포스 이용해도 괜찮음
    for mushroom in arr:
        sum += mushroom
        # 100과의 차이의 절댓값이 여태까지의 최소 차이보다 작거나 같다면 -> 이게 최대 점수
        # 마리오는 큰 값을 택해야하므로 작거나 같아야 한다.
        if diff >= abs(100 - sum):
            diff = abs(100 - sum)
            answer = sum

    return answer

maximum_score = calc_score(mushroom_list)
print(maximum_score)