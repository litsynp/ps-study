# p.217 다이나믹 프로그래밍 - 1로 만들기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

X = int(input())

d = [0] * 30001

# Bottom-up 방식
for i in range(2, X + 1):
    d[i] = d[i - 1] + 1

    if i % 5 == 0:
        d[i] = d[i // 5] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[X])
