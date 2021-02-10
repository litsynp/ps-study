# p.92 그리디 - 큰 수의 법칙
# Simple solution
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)

ans = 0
count = 0

for i in range(M):
    if count < K:
        ans += arr[0]
        count += 1
    else:
        ans += arr[1]
        count = 0

print(ans)
