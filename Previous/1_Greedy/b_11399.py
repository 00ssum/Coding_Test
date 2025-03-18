n= int(input())

line=list(map(int,input().split()))
line.sort()

sum=0
for i in range(len(line)):
    for j in range(0,i+1):
        sum+=line[j]


print(sum)
