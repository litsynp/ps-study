# p.87 거스름돈
import sys

input = sys.stdin.readline

coins = [500, 100, 50, 10]
N = int(input())
ans = []

for coin in coins:
    ans.append(int(N / coin))
    N = N % coin

print(sum(ans))
