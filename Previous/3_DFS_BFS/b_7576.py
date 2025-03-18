from collections import deque
m,n=map(int,input().split())
g=[]
for i in range(n):
    g.append(list(map(int,input().split())))


q=deque()
for i in range(n): #1이 들어있는곳을 배열에 담음
    for j in range(m):
        if g[i][j] == 1:
            q.append((i, j))

res=0
#함수
def bfs():
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if (n>nx >= 0) and (m>ny>=0):
                if g[nx][ny]==0: #익지 않은 상태면
                    g[nx][ny] = g[x][y]+1
                    q.append((nx,ny))

bfs()
for i in g:
    for j in i:
        if j == 0: #g에 0이 남아 있으면
            print(-1)
            exit(0)
    res = max(res, max(i))#[ , , ,,,, ]->에서 가장 큰값=가장 오래 걸리는 경로= 걸리는 요일
# 처음 시작을 1로 표현했으니 1을 빼준다.
print(res - 1)
