import random


def quickSort(S):

    def partition(i, j):
        pivot_idx = random.randint(i, j)
        pivot = S[pivot_idx]
        S[pivot_idx], S[j] = S[j], S[pivot_idx]

        store = i
        for k in range(i, j):
            if S[k] < pivot:
                S[store], S[k] = S[k], S[store]
                store += 1

        S[store], S[j] = S[j], S[store]
        return store

    def sort(i, j):
        if i >= j:
            return

        mid_idx = partition(i, j)
        sort(i, mid_idx - 1)
        sort(mid_idx + 1, j)

    sort(0, len(S)-1)
    return S


S = [1, 2, 5, 4, 2, 7, 10, 8, 7]
print(quickSort(S))