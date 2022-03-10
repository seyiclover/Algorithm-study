def solution(n, s, t):
    newS = list(s)
    if t < n:
        result = '.' * (n-t) + newS[:t]

    return result
