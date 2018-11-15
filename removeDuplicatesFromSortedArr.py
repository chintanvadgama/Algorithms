# Use slow and fast pointers
class Solution(object):
    def removeDuplicates(self, arr):
        n = len(arr)
        if n == 0 or n == 1:
            return n

            # To store index of next
        # unique element
        j = 0

        # Doing same as done
        # in Method 1 Just
        # maintaining another
        # updated index i.e. j
        for i in range(0, n - 1):
            if arr[i] != arr[i + 1]:
                arr[j] = arr[i]
                j += 1

        arr[j] = arr[n - 1]
        j += 1
        print(arr[:j])
        return j


def removeduplicates_usingset(arr):
    freq = {}
    for a in arr:
        if a not in freq:
            freq[a] = 1
    print(freq)
    return freq.keys()


print(removeduplicates_usingset([1, 2, 2, 3, 4, 4, 4, 5, 5]))

print Solution().removeDuplicates([1, 2, 2, 3, 4, 4, 4, 5, 5])
