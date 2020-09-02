def findCandidate(A):
    maj_index = 0
    count = 0
    for i in range(len(A)):
        if count == 0:
            maj_index = i
            count = 1

        elif A[maj_index] == A[i]:
            count += 1
        else:
            count -= 1

    return A[maj_index]


A = [1, 1, 2, 2, 1]
print(findCandidate(A))
"""
To be Noted:
    1. if it is guaranteed that there must be a major element, then the output must be the desired answer
    2. if not, then the output makes no sense at all. Must iterate again to check if it is the major element.
"""