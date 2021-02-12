# p.182 정렬 - 두 배열의 원소 교체
"""
5 3
1 2 5 4 3
5 5 6 6 5

10 5
1 1 5 6 11 5 8 9 10 23
4 3 1 4 5 3 2 1 5 1
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

count = 0
for i in range(K):
    # B에 A보다 큰 것이 없다면 더 이상 볼 필요가 없음
    if A[i] > B[i]:
        break

    A[i], B[i] = B[i], A[i]

print(sum(A))
