# p.220 다이나믹 프로그래밍 - 개미 전사
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * (N + 1)

# 1개의 식량창고가 있다면 그 하나만 터는 것이 정답
dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

# 식량 창고의 개수를 하나씩 늘려 가며 DP 테이블 갱신
for i in range(2, N):
    # 직전 칸까지의 정답 v.s. 두 칸 이전까지의 정답 + 현재 칸의 식량
    dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

print(dp[N - 1])
# p.220 다이나믹 프로그래밍 - 개미 전사
"""
4
1 3 1 5
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N

# 1개의 식량창고가 있다면 그 하나만 터는 것이 정답
dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

# 식량 창고의 개수를 하나씩 늘려 가며 DP 테이블 갱신
for i in range(2, N):
    # 직전 칸까지의 정답 v.s. 두 칸 이전까지의 정답 + 현재 칸의 식량
    dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

print(dp[N - 1])
