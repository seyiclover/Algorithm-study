# s1이 긴 문자열 s2가 짧거나 길이가 같은 문자열 이라고 정의
# s2의 약수에 해당하는 문자열을 구한다. 
# s2의 각 약수를 곱해서 s1을 만들 수 있는 지 확인하고 가장 긴 약수에 해당하는 문자열을 출력한다. 

<내 코드>
def solution(s1, s2):

    if len(s2) > len(s1):
        s1, s2 = s2, s1

    n = len(s2)
    for i in range(n):
        for j in range(i+1):
            token = s2[j:n-i+j]
           
            if token in s1:
                return token
    else:
        return ''
      
      
<정답코드>
def solution(s1, s2):
  def isDivisor(string, divisor):
    n = len(divisor)
    # 최대공약문자열이 존재하려면 두 문자열의 길이가 최대공약수를 가져야 한다. 
    if len(string) % n != 0:
      return False
    # 나누는 문자열의 길이만큼 긴 문자열을 슬라이싱 했을 때 동일하다면 True를 반환하게 된다. 
    while string != '':
      if string[:n] != divisor:
        return False
      string = string[n:]              # 문자열의 없는 인덱스를 지정해서 슬라이싱하면 공백 문자가 된다. => ''로 출력됨 
    return True

  # 길이가 긴 문자열을 str1, 길이가 짧거나 같은 문자열을 str2로 지정 
  if len(s1) > len(s2):
    str1, str2 = s1, s2
  else:
    str1, str2 = s1, s2
    
  divisor = str2
  m = 1
  while divisor != '':
    if isDivisor(str2, divisor) and isDivisor(str1, divisor): 
      return divisor
    m += 1
    divisor = str2[:len(str2) // m]
  return ''
