"""
Kadane's Algorithm
    1. max_to_this_point = max(max_to_this_point + x, x)
    2. max_so_far = max(max_so_far, max_to_this_point)
"""

import time

def maxSumSubarray(arr):
    max_this_point = float('-inf')
    max_so_far = float('-inf')
    for x in arr:
        max_this_point = max(max_this_point + x, x)
        max_so_far = max(max_so_far, max_this_point)
    return max_so_far


# improvement 1: if local sum < 0, update sum = 0
def maxSumSubarray1(arr):
    max_this_point = float('-inf')
    max_so_far = float('-inf')
    for x in arr:
        max_this_point += x
        if max_this_point < 0:
            max_this_point = 0
        max_so_far = max(max_so_far, max_this_point)
    return max_so_far


# improvement 2: if all elements are negative
def maxSumSubarray2(arr):
    max_this_point = arr[0]
    max_so_far = arr[0]
    for x in arr:
        max_this_point = max(max_this_point + x, x)
        max_so_far = max(max_so_far, max_this_point)
    return max_so_far


# improvement 3: print the sub-array with largest sum
def maxSumSubarray3(arr):
    max_this_point = arr[0]
    max_so_far = arr[0]
    l, r = 0, 0
    for i, x in enumerate(arr):
        if max_this_point + x < x:
            max_this_point = x
            l = i
        else:
            max_this_point += x

        if max_so_far < max_this_point:
            max_so_far = max_this_point
            r = i

    return arr[l: r+1]


arr = [-2, -3, 4, -1, -2, 1, 5, -3, -2, 1, -3, 4, -1, -2, 1, 5, -3, -3, 4]

start = time.time()
print(maxSumSubarray(arr))
print(time.time() - start)

start = time.time()
print(maxSumSubarray1(arr))
print(time.time() - start)

start = time.time()
print(maxSumSubarray3(arr), sum(maxSumSubarray3(arr)))
print(time.time() - start)


# arr_n = [-2, -3, -4, -1, -2, -1, -5, -3, -2, -3, -4, -1, -2, -1, -8, -3, -4, -1, -2, -1, -5, -3]
# start = time.time()
# print(maxSumSubarray2(arr_n))
# print(time.time() - start)