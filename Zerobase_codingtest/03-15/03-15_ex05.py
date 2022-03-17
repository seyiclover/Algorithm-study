<내 풀이>
# 빈 리스트를 만들어 두고 순차적으로 조회하면서 짝수일 때는 한번, 홀 수 일 때는 두 번 빈 리스트에 추가해 준다. 
# 결과 값은 arr 배열의 길이만큼만 인덱싱한다. 

def solution(arr):

    newArr = []  

    for i, v in enumerate(arr):
        if v % 2 ==0:
            newArr.append(v)
        else:
            newArr.append(v)
            newArr.append(v)


    return newArr[:len(arr)]
  
  <정답코드>
  def solution(arr):

    result = []

    i = 0
    while len(result) < len(arr):
        element = arr[i]
        result.append(element)
        if element % 2 == 1 and len(result) < len(arr):
            result.append(element)

        i += 1

    return result
