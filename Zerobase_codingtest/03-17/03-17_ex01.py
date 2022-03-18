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
    if len(string) % n != 0:
      return False
    while string != '':
      if string[:n] != divisor:
        return False
      string = string[n:]
    return True
 
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
