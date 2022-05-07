# 효율적으로 탐색을 하기 위해 dfs(깊이 우선 탐색) 알고리즘 사용 

<정답 풀이>

def solution(n, m, patterns):
    n_p = len(patterns)
    min_turn = float('inf')    # 양의 무한대 
    
    def dfs(turn, monster, player):  # 차례, 몬스터 체력, 플레이어 체력
        nonlocal min_turn    # nonlocal: 중첩함수에서 global 키워드처럼 사용할 수 있다. 

        if turn >= 199:
            return
        if turn >= min_turn:
            return
        # 플레이어는 대기 시 1턴 후, 공격 시 2턴 후, 회피 시 3턴 후에 동작할 수 있음
        p0 = patterns[turn % n_p] # 대기
        p1 = patterns[(turn + 1) % n_p] # 공격
        p2 = patterns[(turn + 2) % n_p] # 회피  
        
        # 몬스터 체력 1, 대기했을 때 이후 몬스터의 행동이 대기이거나 플레이어의 체력이 1이상이라면 공격 횟수를 늘려주다. 
        if monster == 1 and (p0 == 0 or player > 1):  
            min_turn = min(turn + 1, min_turn)
            return

        if p0 == 0:
            if p1 == 0:
                dfs(turn + 2, monster - 1, player)
            if p1 == 1 and player > 1:
                dfs(turn + 2, monster - 1, player - 1)
        else:
            if p1 == 0 and player > 1:
                dfs(turn + 2, monster - 1, player - 1)
            if p1 == 1 and player > 2:
                dfs(turn + 2, monster - 1, player - 2)
        if p2 == 0:
            dfs(turn + 3, monster, player)
        if p2 == 1 and player > 1:
            dfs(turn + 3, monster, player - 1)

    dfs(0, n, m)
    return min_turn if min_turn <= 200 else -1
