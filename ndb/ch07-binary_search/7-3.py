# p.201 이진 탐색 - 떡볶이 떡 만들기
"""
4 6
19 15 10 17
"""

import sys
input = sys.stdin.readline


def binary_search_rk(arr, M, start, end):
    result = 0

    # 절단기의 높이를 조절하는 이진 탐색
    while start <= end:
        # mid: 현재 절단기의 높이
        mid = (start + end) // 2

        # total: 절단기로 자르고 남은 떡의 길이 합
        total = sum([x - mid for x in arr if x > mid])

        if total < M:
            # 남은 떡의 길이 합이 목표보다 부족하면, 더 낮은 곳에서 자른다
            end = mid - 1
        else:
            # 남은 떡의 길이 합이 목표보다 많으면, 더 낮은 곳에서 잘라본다
            # 자르기 전에 이전의 값을 저장함으로써 M을 만족하는 최대값을 구한다
            result = mid
            start = mid + 1

    return result


N, M = map(int, input().split())
arr = list(map(int, input().split()))

maximum = max(arr)
result = binary_search_rk(arr, M, maximum - M, maximum)
print(result)
