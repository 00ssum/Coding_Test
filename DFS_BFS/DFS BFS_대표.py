#BFS: 미로 찾기, 경로찾기-----
#입력
from collections import deque
n,m=map(int,input().split())
g=[]
for i in range(n):
    g.append(list(map(int,input())))
#함수
def bfs(x,y):
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if (n>nx >= 0) and (m>ny>=0) :
                if g[nx][ny]==1:
                    g[nx][ny] = g[x][y]+1
                    q.append((nx,ny))
    return g[n-1][m-1]

print(bfs(0,0))

#DFS: 묶음찾기=================
#입력
M, N, K = map(int, input().split())
g = [[0]*M for _ in range(N)]
cnt = 0

for i in range(N):  # 행 (바깥 리스트)
  for j in range(M):  # 열 (내부 리스트)
    if g[i][j] > 0:
      dfs(i, j)
      cnt += 1

#함수
def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 상,하,좌,우 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M):
            if g[nx][ny] == 1: # 1발견하면
                g[nx][ny] = -1 #방문 했다고 표시함
                dfs(nx, ny) #재귀 호출
