"""
Given an array of values and a K value (K < number of elements in array), return the sorted list of top K values.

Example:
A = [6, 3, 7, 8, 1, 4, 9]
K = 3
Answer = [9, 8, 7]
"""
import heapq


def findTopElements(arr, k):
    if not arr:
        return []
    if len(arr) < 2:
        return arr[0]

    heap = []
    for item in arr:
        # if we haven't find k or current item is larger than smallest in arr
        # arr = 1000, k = 3, heap = 1
        if len(heap) < k or item > heap[0]:
            if len(heap) == k:
                heapq.heappop(heap)
            heapq.heappush(heap, item)

    return sorted(heap, reverse=True)


if __name__ == '__main__':
    A = [6, 3, 7, 8, 1, 4, 9, 9, 9]
    K = 3

    answer = findTopElements(A, K)
    print(answer)
    #  array=  [6, 3, 7, 8, 1, 4, 9,9,9]
