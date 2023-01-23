from collections import deque
#DFS---------------------------------
def DFS(graph, root):
    visited = []
    stack = [root]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)

#BFS---------------------------------
def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft() #이번에 방문한 노드-> queue에 앞에서 부터 한개씩 꺼냄
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort() #자식 노드들 정렬
                queue += temp # 자식노드들을-> 다음 step에 순회 할 노드로 정함
    return " ".join(str(i) for i in visited)

#input---------------------------------
node, edge, start = map(int,input().split())

#엣지 연결 입력 받기  (dict)
graph = {}
for i in range(edge):
    n1, n2 = map(int,input().split())
    #n1->n2
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)
    #n2->n1
    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)
''' 
#직접 초기화 해줘도 됨
graph={1: [2, 3, 4],
       2: [1, 4], 
       3: [1, 4], 
       4: [1, 2, 3]}
'''

print("DFS: ",DFS(graph, start))
print("BFS: ",BFS(graph, start))
