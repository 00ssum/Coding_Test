#https://www.acmicpc.net/problem/10825
'''
1. 국어 점수가 감소 순서
2. 국어 점수가 같으면->  영어 점수가 증가하는 순서
3. 국어 점수와 영어 점수가 같으면->  수학 점수가 감소하는 순서
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문보다 앞에 옴)

'''
N = int(input())
arr = []

for _ in range(N):
    name,k,e,m = list(input().split())
    arr.append([name, int(k),int(e),int(m)])

arr.sort(key = lambda x : (-x[1], x[2],-x[3],x[0]))

for i in arr:
    print(i[0])
