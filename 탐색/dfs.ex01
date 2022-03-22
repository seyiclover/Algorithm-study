# n행 m열 입력 
n, m = map(int, input().split())

# 맵 정보 입력 
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS 탐색 상하좌우 노드 방문 
def dfs(x, y):
    # 맵 범위를 벗어날 경우 종료
    if x <= -1 or x > n or y <= -1 or y > m:
        return False
    # 방문하지 않은 노드 방문표시 
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상하좌우 위치 방문
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True
    return False

# 아이스크림 개수 세기
cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1

print(cnt)
