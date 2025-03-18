import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, d, start = map(int,input().split())

# 각 노드에 연결되어 있는, 노드에 대한 정보
#최단 경로=> 디익스트라 사용

graph = [[] for i in range(n + 1)]
# 최단 거리 테이블, 무한으로 초기화
distance = [INF] * (n + 1)

#모든 간선 정보
for _ in range(m):
    a, b = map(int, input().split()) # a->b 비용 c
    graph[a].append((b, 1))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# start노드에 대한 다익스트라 알고리즘
dijkstra(start)
c=0
# start -> 모든 노드의 최단 거리
for i in range(1, n + 1):
    if distance[i] == d: #연결 안됨
        c+=1
        print(i)
if c==0:
    print(-1)
