n=int(input())

dp=[]
for i in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1,n): #줄
    for j in range(i+1):#객체
        if j==0: #맨 왼쪽
           u_l=0
        else:#왼쪽 위 노드
            u_l=dp[i-1][j-1]

        if j==i:# 맨 오른쪽
           up=0
        else:#오른쪽 위 노드
            up=dp[i-1][j]

        dp[i][j]=dp[i][j]+ max(u_l,up)

print(max(dp[n-1]))

----------------------------------
밑=> 위로 올라가는 계산법
n = int(input())
a = []

for i in range(n):
    a.append(list(map(int,input().split())))

for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        k= a[i + 1][j]
        h= a[i + 1][j + 1]
        a[i][j] += max(a[i + 1][j], a[i + 1][j + 1])

print(a[0][0])
