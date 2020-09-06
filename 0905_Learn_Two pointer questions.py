"""
    Use <Two Pointers> method in two-sum or three-sum questions
"""
import bisect

# The input array is sorted, therefore we can use two pointers method
def twoSum1(arr: [int], target: int) -> [int]:
    l, r = 0, len(arr) - 1
    while l < r:
        summ = arr[l] + arr[r]
        if summ == target:
            return [l + 1, r + 1]
        elif summ > target:
            r -= 1
        else:
            l += 1

    return [-1, -1]


def twoSumSmallerThanK1(arr: [int], K: int) -> int:
    """
    returns the largest sum that smaller than K.
    If no ans, return -1
    :param arr:
    :param K:
    :return:
    """

    arr.sort()
    l, r = 0, len(arr) -1
    ans = -1

    while l < r:
        summ = arr[l] + arr[r]
        if summ < K:
            ans = max(ans, summ)
            l += 1
        else:
            r -= 1
    return ans


def testFunction():
    arr1 = [2, 7, 11, 15]
    target = 9

    print(twoSum1(arr1, target))

    arr2 = [34, 23, 1, 24, 75, 33, 54, 8]
    print(twoSumSmallerThanK1(arr2, K=60))


testFunction()