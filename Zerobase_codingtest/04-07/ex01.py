# 내 풀이 
# 문자열을 거꾸로 나열해준뒤 숫자와 문자를 판별하여 계산에 넣어준다. 

def solution(n, probs):
    result = []
    reverse = []
    char = ''
    value = 0
    for i in probs:
        for j in i:
            char = j + char
        reverse.append(char)
        char = ''
    for i in reverse:
        for idx, j in enumerate(i):
            if j.isdigit():
                value += (n ** idx) * int(j)
            else:
                if j.isupper():
                    value += (n ** idx) * (ord(j) - 29)
                else:
                    value += (n ** idx) * (ord(j) - 87)
        result.append(value)
        value = 0

    return result
  
# 정답코드 
def solution(n, probs):
    # 문제의 기준에 맞게 문자별로 숫자 업데이트 
    mapper = {str(i): i for i in range(10)}
    mapper.update({chr(ord('a') + i): len(mapper) + i for i in range(ord('z') - ord('a') + 1)})
    mapper.update({chr(ord('A') + i): len(mapper) + i for i in range(ord('Z') - ord('A') + 1)})
    
    results = [0 for _ in range(len(probs))]
    for i , prob in enumerate(probs):
        for j in range(len(prob)):
            p = len(prob) - j - 1
            results[i] += mapper[prob[j]] * n ** p
            
    return results
            
# 참고 풀이 
def solution(n, probs):
    BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char_list = [str(each) for each in BASE62]

    answer = []
    for word in probs:
        tmp = []
        cnt = 0
        for char in reversed(word):
            idx = char_list.index(char)
            tmp.append(idx * (n**cnt))
            cnt+= 1

        answer.append(sum(tmp))

    return answer
  
 # 참고 풀이 2 
 def solution(n, probs):
    probslist = []

    for prob in probs:
        idx = 0
        result = 0
        for ele in prob[::-1]:
            if ele.isnumeric() == True:
                result += int(ele) * (n ** idx)
            elif ele.islower() == True:
                result += (ord(ele)-87) * (n ** idx)
            elif ele.isupper() == True:
                result += (ord(ele)-29) * (n ** idx)
            idx += 1
        probslist.append(result)
    return probslist
        
    
