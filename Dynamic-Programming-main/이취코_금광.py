t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # 각 위치에서의 최대 이익을 저장할 배열
    dp = []
    index = 0
    for _ in range(n):
        dp.append(data[index:index + m]) #이차원 배열로 저장
        index += m

    for j in range(1, m): #열 갯수
        for i in range(n): #행 갯수
        # 대각선 위에서 옴:  dp[i - 1][j - 1]
        # 바로 옆 이동: dp[i][j - 1]
        # 대각선 아래에서 옴: dp[i + 1][j - 1] 

            if i == 0:# 가장 위 행 (바로 옆, 대각선 아래에서 옴)
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j - 1])+ dp[i][j]

            elif i == n - 1: #가장 아래 행 (바로옆, 대각선 위에서 옴)
                dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1])+ dp[i][j]

            else: # 중간 행 (바로옆, 대각선위, 대각선 아래)
                dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])+ dp[i][j]
    ans = 0
    for i in range(n):
        ans = max(ans, dp[i][m - 1])
    print(ans)

