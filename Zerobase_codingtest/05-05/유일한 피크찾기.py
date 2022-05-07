<내 풀이>
# 최댓값과 그 인덱스를 찾아주는 함수 사용 >> 시간초과 >> 시간 복잡도를 해결하기 위해 함수 사용을 자제해야 한다.  

def solution(x):
    p = max(x)
    index = x.index(p)
    return index
  
  
<정답 풀이>
# 주어지는 리스트의 구조는 점점 value값이 커지다가 peak를 최고점으로 점점 낮아진다. 
# 이진탐색을 활용하여 시간 복잡도를 해결 

def solution(x):
  start, end = 0, lend(x) - 1
  
  while start < end:
    mid = (start + end) // 2
    
    if x[mid - 1] < x[mid]:
      if x[mid + 1] < x[mid]:
        return mid
      else: 
        start = mid
    else:
      end = mid
   return -1
        
