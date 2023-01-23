n, k=map(int,input().split())
cont=0
a=[]
for i in range(n):
    a.append(int(input()))

a.sort(reverse=True)

for i in a:
    if i > k:
        continue
    else:
        cont+= k // i
        k-=(k // i)*i

print(cont)
