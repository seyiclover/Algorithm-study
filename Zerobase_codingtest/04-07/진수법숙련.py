# 내 풀이 
# 문자열을 거꾸로 나열해준뒤 숫자와 문자를 판별하여 계산에 넣어준다. 
# 문자열을 거꾸로 나열해주는 여러 방식 1) reversed(words)를 사용하면 해당 문자열을 거꾸로 조회 2) for word in wrods[::-1] 를 사용하면 거꾸로 조회
#                                    3) 빈 문자열(a)을 만들어서 반복문을 조회하며 빈문자열 앞에 조회된 글자를 넣어준다. 

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

    return answer진수법 숙련
문제
병렬이는 n진수법으로 쓰여진 숫자를 십진수로 변환하는 프로그램을 개발하려고 한다. n진수의 숫자는 문자열로 표현되며, 각 숫자는 아래 문자를 이용해 표현된다.

0 ~ 9 : "0"~"9"
10 ~ 35 : "a" ~ "z"
36 ~ 61 : "A" ~ "Z"
예를 들어 n = 14일 때, "4b"은 아래와 같이 변환할 수 있다.

"4b" = 4*14 + 11 = 67
총 m개의 문자열이 probs 리스트로 주어질 때, 모든 문자열을 십진수로 변환하여 길이가 m인 리스트로 반환하시오.

입력설명
매개변수 n과 probs가 주어지며, 아래 조건을 만족한다.

2 <= n <= 62
m = len(probs)
0 < m <= 100000
0 <= probs[i]를 십진수 변환한 숫자 <= 100000000
출력설명
정수로 이루어진 길이가 m인 리스트를 반환하시오.

매개변수 형식
n = 16
probs = ["94c6", "31db", "8a0a", "5bd2", "7796"]

반환값 형식
[38086, 12763, 35338, 23506, 30614]
  
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
        
    
