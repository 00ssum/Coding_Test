'''
집갯수 n
모든 집까지의 거리가 최소값이 되도록
한 위치에 집 여러개 가능
'''
#https://www.acmicpc.net/problem/18310

n = int(input())
arr=list(map(int, input().split()))
arr.sort()

print(arr[(n-1)//2])
