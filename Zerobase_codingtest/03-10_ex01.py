# 전광판의 크기(*)와 노출할 글자를 합쳐서 전체 글자로 보고 어디서부터 어디까지 인덱싱할 것인지로 단순화하는 것이 핵심 아이디어
def solution(n, s, t):
    # 노출할 글자 전체(*가 앞뒤로 노출될 것이므로 입력)
    word = ("." * n) + s + ('.' * (n-1))
    # 인덱싱 시작 지점
    t = t % len(word)

    result = word[t:t+n]

    return result
