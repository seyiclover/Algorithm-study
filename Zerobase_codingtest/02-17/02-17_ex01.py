import collections

def solution(S):

    answer = ''
    nH = collections.defaultdict(int)

    for x in s:
        nH[x] += 1

    tmp = sorted(nH.items(), key=lambda x: (x[1], -ord(x[0])), reverse=True)

    for key, frq in tmp:
        answer += key*frq

    return answer 
