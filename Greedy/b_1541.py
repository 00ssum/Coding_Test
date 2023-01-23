arr = input().split('-')
s = 0

for i in arr[0].split('+'): #처음 -가 나올때까지
    s += int(i)#모든 수 더함

for i in arr[1:]: #- 등장
    for j in i.split('+'): # + 기준으로 분리
        s -= int(j) # 빼줌
print(s)
