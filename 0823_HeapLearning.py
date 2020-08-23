"""
Heap: a complete binary tree that satisfies the heap priority

Complete Binary Tree:
    1. Every level, except the last, is filled
    2. Every node is as far left as possible

Max / Min Heap:
    Each node is always larger / smaller than its children

Heap Operations: Heapify
    1. heapify
    2. insert a new num
    3. delete a num

"""


def heapify(arr: [int], size: int, i: int):
    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and arr[left] > arr[i]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)


def insert(arr: [int], num: int):
    arr.append(num)
    size = len(arr)

    for i in range(size // 2 - 1, -1, -1):
        heapify(arr, size, i)


def delete(arr: [int], num: int):
    size = len(arr)
    for i, n in enumerate(arr):
        if n == num:
            break

    arr[size - 1], arr[i] = arr[i], arr[size - 1]
    arr.remove(size-1)

    for i in range((size-1)//2 - 1, -1, -1):
        heapify(arr, size-1, i)


arr = []
insert(arr, 3)
print(arr)
insert(arr, 9)
print(arr)
insert(arr, 5)
print(arr)
insert(arr, 1)
print(arr)
insert(arr, 4)
print(arr)
insert(arr, 2)
print(arr)

delete(arr, 4)
print(arr)

