# p.197 이진 탐색 - 부품찾기
"""
5
8 3 7 9 2
3
5 7 9
"""

import timeit

# ======================================== #
# from random import randint

# N = randint(0, 100000)
# parts = [randint(0, 100000) for x in range(N)]

# M = randint(0, 100000)
# requested = [randint(0, 100000) for x in range(M)]

# print(N, M)
# ======================================== #

import sys
input = sys.stdin.readline


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


N = int(input())
parts = sorted(list(map(int, input().split())))
M = int(input())
requested = list(map(int, input().split()))

# ======================================== #
start_time = timeit.default_timer()
# ======================================== #

for item in requested:
    result = binary_search(parts, item, 0, N - 1)
    print('no' if result == None else 'yes', end=' ')

# ======================================== #
end_time = timeit.default_timer()
exec_time = end_time - start_time
print('Total execution time: %fs' % exec_time)
# ======================================== #
