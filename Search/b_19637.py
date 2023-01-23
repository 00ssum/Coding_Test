import bisect
import sys
inpit

N, M = map(int, sys.stdin.readline().split())

calls = []
powers = []
for _ in range(N):
    a, b = sys.stdin.readline().split()
    calls.append(a)
    powers.append(int(b))

for _ in range(M):
    temp = int(sys.stdin.readline().rstrip())
    print(calls[bisect.bisect_left(powers, temp)])
