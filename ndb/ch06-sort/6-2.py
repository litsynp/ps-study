# p.178 정렬 - 위에서 아래로
"""Test case
3
15
27
12
"""

import sys
input = sys.stdin.readline


def quick_sort(arr, start, end):
    """내림차순 정렬"""
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] >= arr[pivot]:
            left += 1
        while right > start and arr[right] <= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

quick_sort(arr, 0, len(arr) - 1)

for i in arr:
    print(i, end=' ')
