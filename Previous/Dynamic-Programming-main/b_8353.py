```python
n = int(input())
a=list(map(int, input().split()))
a.reverse()
dp = [1] * n
# 앞쪽에 있는 값이 항상 뒤보다 커야함
# 남아있는 병사 수가 최대가 되어야 함

for i in range(1, n): # 타겟 병사 (앞)
    for j in range(0, i): #비교 할 뒤에 병사 (뒷부분)
        if a[j] < a[i]: #만약에 뒤에가 더 클 경우
            dp[i] = max(dp[i], dp[j]+1) #길이에 +1
print(n - max(dp))
```
