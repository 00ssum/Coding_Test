import sys
from collections import deque
input = sys.stdin.readline()

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k: #도착했을 때
            return(dist[x]) #해당하는 노드에 담긴 거리

        for j in (x-1, x+1, x*2):
            if (0<= j <= MAX) and (dist[j]==0):
                dist[j] = dist[x] +1
                q.append(j)

MAX = 100000
n,k = map(int,input.split())
dist = [0] * (MAX+1) #방문 해주지 않은곳을 0으로

print(bfs())
