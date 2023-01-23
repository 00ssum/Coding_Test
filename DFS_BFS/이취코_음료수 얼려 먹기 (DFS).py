def dfs(x,y):
    # 주어진 범위 벗어남
    if x<= -1 or x>= n or y <= -1 or y >= m :
        return False

    if graph[x][y] == 0: #방문하지 않은 노드면
        graph[x][y] = 1 # 방문 처리

        #상하좌우 재귀적 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

#_---------------------------------------------
n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# 모든 노드 탐색, 0이 몇 묶음인지 확인
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
print(result)
