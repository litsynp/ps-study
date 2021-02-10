# p.99 그리디 - 1이 될 때까지
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 연산 횟수
ans = 0

# N이 1이 될 때까지,
# N이 K로 나누어 떨어지면 나눗셈, 아니면 뺄셈
while N != 1:
    if N % K == 0:
        N //= K
    else:
        N -= 1

    ans += 1

print(ans)

# ========================================
# 코드 더 줄여보기
# ========================================
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# ans = 0

# while N != 1:
#     N = N // K if N % K == 0 else N - 1
#     ans += 1

# print(ans)
# ========================================
