<내 풀이>

def solution(area):
    # 주어진 값으로 만들 수 있는 [가로, 세로] 경우를 리스트로 만들어 준다.
    case = []
    for i in range(1, area):
        case.append([i, area-i])

    # 최솟값 초기화를 위해 첫번째 인덱스의 가로 세로 차이값을 넣어준다.
    # 인덱스 차이를 순회하면서 차이값이 최소인 리스트를 저장해준다.
    minimum = abs(case[0][0] - case[0][1])
    minimumItem = ''
    for item in case:
        if minimum >= abs(item[0] - item[1]):
            minimum = abs(item[0] - item[1])
            minimumItem = item

    return minimumItem

print(solution(5))


<정답코드 수정>
# 주어진 값을 근사하게 두 개의 값으로 나눠야 함
# 가로는 area를 2로 나눈 몫(w), 세로는 area-w

import math

def solution(area):

    w = area // 2
    return [w, area-w]
