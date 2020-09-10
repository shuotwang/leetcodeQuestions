def getMaxInt():
    return (1 << 31) - 1


def getMinInt():
    return -(1 << 31)


def mul2(a):
    return a << 1


def div2(a):
    return a >> 1


def interchange(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b


def oddOccurance(arr):
    ans = 0
    for each in arr:
        ans = ans ^ each
    return ans


"""
Update on Sep 10, 2020
    LeetCode 338. Counting Bits
    Given a non negative integer number num. 
    For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation 
    and return them as an array.
"""


def countBits(num: int) -> [int]:
    ans = [0]

    for i in range(1, num + 1):
        ans.append(ans[i // 2] + i % 2)
    return ans


print(getMaxInt())
print(getMinInt())
print(mul2(5))
print(div2(10))
print(interchange(3, 9))
print(oddOccurance([1, 2, 3, 2, 3, 1, 3]))
print(countBits(10))
