n=int(input())
coin=list(map(int, input().split()))
coin.sort()

target=1 #더해서 만들수 있는 최대값 목표

for i in coin:
    if target<i: #조합의 최대값 목표 보다-> 돈 i의 단위가 크면 break
        break
    target+=i

print(target)
