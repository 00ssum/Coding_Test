mini=[]
n, m=map(int, input().split())
for i in range(n):
    data=list(map(int, input().split()))
    mini.append(min(data))

print(max(mini))
