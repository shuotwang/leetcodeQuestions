"""
You are given a list of n-1 integers and these integers are in the range of 1 to n.
There are no duplicates in the list.
One of the integers is missing in the list.
Write an efficient code to find the missing integer.
"""


# 1. sum subtraction
def missingNum(n: int, arr: [int]) -> int:
    return int((n * (n + 1) / 2) - sum(arr))


# 2. convert index position
def missingNum2(n: int, arr:[int]) -> int:
    for each in arr:
        if 0 <= each - 1 < n - 1:
            arr[each - 1] = abs(arr[each - 1]) * -1

    for each in arr:
        if each > 0:
            return each - 1

arr = [1, 2, 4, 5, 6]
n = 6
print(missingNum(n, arr))
print(missingNum2(n, arr))