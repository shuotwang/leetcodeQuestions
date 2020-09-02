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


print(getMaxInt())
print(getMinInt())
print(mul2(5))
print(div2(10))
print(interchange(3, 9))
print(oddOccurance([1, 2, 3, 2, 3, 1, 3]))
