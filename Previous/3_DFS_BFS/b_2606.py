node=int(input())
edge=int(input())

g={}
for i in range(edge):
    n1,n2=map(int,input().split())
    if n1 not in g:
        g[n1]=[n2]
    elif n2 not in g[n1]:
        g[n1].append(n2)

    if n2 not in g:
        g[n2]=[n1]
    elif n1 not in g[n2]:
        g[n2].append(n1)


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
    return len(visited)-1

print(DFS(g, 1))
