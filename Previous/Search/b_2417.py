import sys
input= sys.stdin.readline
n = int(input())

start= 0
end = n

while True:
    mid = (start+end) // 2

    if end < start:
        break

    if mid**2 < n: # n> mid제곱: mid값을 키움
        start = mid + 1
    else: # mid제곱> n : mid값을 줄임
        end = mid - 1

print(end+1)
