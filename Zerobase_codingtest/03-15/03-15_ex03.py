< 내 코드 >
# 1
def solution(bridge, jumpSize):

    finder = 0
    highest = 0

    for i in bridge:
        if i == 0:
            finder += 1
        else:
            if finder > highest:
                highest = finder
            finder = 0

    maxLen = highest+1
    if maxLen <= jumpSize:
        return True
    else:
        return False
    
    
# 2
def solution(bridge, jumpSize):

    cnt = 0
    flag = True
    
    for i in bridge:
        if i == 0:
            cnt += 1
        if i ==1:
            if cnt <= jumpSize:
              cnt = 0
            else:
              flag = False
              
    return flag
              
              

<정답코드>
def solution(bridge, jumpSize):
    """
    :param bridge: int[]
    :param jumpSize: int
    :return: boolean
    """

    lastStoneIndex = 0
    for i in range(len(bridge)):
        if bridge[i] == 1:
            distance = i - lastStoneIndex - 1
            if distance > jumpSize: return False
            lastStoneIndex = i

    return True
