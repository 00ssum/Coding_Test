n = int(input())
d=[0]*1001

a=[2,3,5]
d[1]=1


k=2
for i in range(2,1001): #타겟수
    for j in range(2,i+1): #비교수
        if i%j==0:
            if j not in a:
                break
            else:
                d[k]=i
                k+=1
                break

print(d[n])
