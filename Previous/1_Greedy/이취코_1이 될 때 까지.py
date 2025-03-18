n, k = map(int, input().split())
cont=0

while n>=k:
    while n % k !=0: #나눠 떨어지지 않으면
        n-=1 #-1
        cont+=1
    n//=k # 나눠 떨어지면 나눔
    cont+=1

while n>1: # 1~(k-1)일때
    n-=1 # -1
    cont+=1

print(cont)
