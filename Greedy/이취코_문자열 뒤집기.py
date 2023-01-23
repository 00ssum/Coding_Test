s=input()
g0=0
g1=0

if s[0]=="1":
    g1+=1
else:
    g0+=1

for i in range(len(s)-1):
    if s[i] != s[i+1]: 
        if s[i+1] == "1":#0->1로 바뀜
            g0 += 1 #0그룹 증가
        else: #1-> 0으로 바뀜 
            g1 += 1# 1그룹 증가

print(min(g1,g0))
