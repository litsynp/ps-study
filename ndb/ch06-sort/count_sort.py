import timeit
# ======================================== #

import random

arr = [random.randint(1, 1_000_000) for i in range(1_000_000)]
# arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]


def count_sort(arr):
    counts = [0] * (max(arr) + 1)

    # counts 배열에 해당 숫자 등장 횟수 추가
    for i in range(len(arr)):
        counts[arr[i]] += 1

    res = []
    for i in range(len(counts)):
        for j in range(counts[i]):
            res.append(i)

    return res


# print(arr)

# ======================================== #
start_time = timeit.default_timer()
# ======================================== #

arr = count_sort(arr)

# ======================================== #
end_time = timeit.default_timer()
exec_time = end_time - start_time
print('Total execution time: %fs' % exec_time)
# ======================================== #

# print(arr)
