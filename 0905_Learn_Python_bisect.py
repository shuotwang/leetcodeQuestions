"""
    1. Bisect left: insert new element in a sorted array, at left-most possible position
"""
import bisect


def twoSumSmallerThanK(arr: [int], K: int) -> int:
    # use binary search method (bisect)
    arr.sort()
    ans = -1
    for i in range(len(arr)):
        j = bisect.bisect_left(arr, K - arr[i], i + 1) - 1
        if j > i:
            ans = max(ans, arr[i] + arr[j])
    return ans


def testFunction():

    arr2 = [34, 23, 1, 24, 75, 33, 54, 8]
    print(twoSumSmallerThanK(arr2, K=60))


testFunction()