import sys
input = sys.stdin.readline

array = list(map(int, input().split()))


def count_sort(array):
    count = [0] * (max(array) + 1)

    for i in range(len(array)):
        count[array[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')
