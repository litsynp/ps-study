# p.226 다이나믹 프로그래밍 - 효율적인 화폐 구성
"""
2 15
2
3

3 4
3
5
7
"""
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
coins = [int(input()) for i in range(N)]
dp = [INF] * 10001

for coin in coins:
    dp[coin] = 1

for i in range(2, M + 1):
    for coin in coins:
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[M] if dp[M] < INF else -1)
