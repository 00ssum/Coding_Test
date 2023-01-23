n=input()
n=list(map(int,n)) #list로 만들어줌
su=0
for i in range(len(n)):
    su=max(su+n[i], su*n[i]) #둘중 큰수로 su업데이트

print(su)
