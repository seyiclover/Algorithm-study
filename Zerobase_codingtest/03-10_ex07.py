def solution(n):
  # 십진수를 2진수로 표현
    binaryNum = format(n, 'b')

    finder = 0
    highest = 0
    for each in str(binaryNum):
        if each == '0':
            finder += 1
        else:
            if finder > highest:
                highest = finder
            finder = 0
    return highest+1


print(solution(5))
  
  
<정답코드>
def solution(n):

    maxDistance = 0
    curDistance = -1

    # n이 0 이하가 될 때까지 반복한다.
    while n > 0:
        # n의 이진 표현중 최초 1이 나올때까지 거리를 재지 않는다.
        if curDistance == -1:
            # n의 이진 표현중 가장 우측값이 1이 나오면 초기화
            if (n & 1) == 1:
                curDistance = 0
        else:
            # 거리를 1 증가 한다.
            curDistance += 1

            # 인접한 1까지의 거리를 계산한다.
            if (n & 1) == 1:
                maxDistance = max(maxDistance, curDistance)
                curDistance = 0

        # n을 우측으로 쉬프트한다.
        n >>= 1

    return maxDistance
