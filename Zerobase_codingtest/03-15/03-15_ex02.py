<내 코드: 0.8점>
def solution(arr):

    cnt = 0
    highest = 0

    for each in arr:
        if each == 1:
            cnt += 1
            # else 아래에 위치하면 배열이 1로 끝날 때는 정확한 값을 도출하지 못한다.
            if cnt > highest:
                highest = cnt
        else:
            cnt = 0

    return highest
  
  

<정답 코드>
def solution(arr):
    """
    :param arr: int[]
    :return: int
    """

    result = 0
    continuedOneCount = 0
    for binary in arr:
        if (binary == 1):
            continuedOneCount += 1
            result = max(result, continuedOneCount)
        else:
            continuedOneCount = 0
            
    return result
