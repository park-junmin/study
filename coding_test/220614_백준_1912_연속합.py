n = int(input())
dp = list(map(int, input().split(" ")))

max_sum = dp[0]

for i in range(1, n):
    dp[i] = max(dp[i], dp[i] + dp[i-1])


print(max(dp))
