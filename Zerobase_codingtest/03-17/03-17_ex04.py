<내 코드>
def solution(nums):

    maxIdx = []
    minIdx = []

    for i, v in enumerate(nums):
        if max(nums) == v:
            maxIdx.append(i)
        if min(nums) == v:
            minIdx.append(i)

    maxLength = len(maxIdx)
    minLength = len(minIdx)

    diff = []
    if maxLength >= minLength: 
        for i in maxIdx:
            for j in minIdx:
                diff.append(abs(i-j))
    if maxLength < minLength:
        for i in minIdx:
            for j in maxIdx:
                diff.append(abs(i-j))

    return min(diff) +1

  <정답 코드>
  def solution(nums):
    max_num = max(nums)
    min_num = min(nums)

    left = 0
    right =0

    answer = len(nums)
    maxs = 1 if max_num == nums[0] else 0
    mins = 1 if min_num == nums[0] else 0
    
    while left <= right:
        if mins > 0 and maxs >0:
            answer = min(answer, right - left + 1)
            if nums[left] == max_num:
                maxs -= 1
            if nums[left] == min_num:
                mins -= 1
            left += 1
        else:
            right += 1
            if right == len(nums):
                break
            if nums[right] == max_num:
                maxs += 1
            if nums[right] == min_num:
                mins+= 1
            
    return answer
