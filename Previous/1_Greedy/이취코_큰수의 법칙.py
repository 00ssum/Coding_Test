n, m, k=map(int, input().split())
data=list(map(int, input().split()))

data.sort(reverse=True)
patt=data[0]*k+data[1] #가장 큰수k번 +두번째로 큰수 1번  => 패턴으로 만듦

sum=(m//(k+1))*patt #패턴만큼 더함
sum+=(m%(k+1))*data[0] #나머지 수만큼 가장 큰수 더해줌
print(sum)
