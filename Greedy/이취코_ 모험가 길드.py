n=int(input())
s=list(map(int,input().split()))
s.sort()

num=0
team=0
for i in s:
    num+=1
    if i <= num:
        team+=1
        num=0
print(team)
