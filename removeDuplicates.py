class Solution:
    def removeDuplicates(self, arr):
        # 1. IF only 1 element in arr
        if len(arr) == 1 or not arr:
            return arr
        # 2. If all elements in array are sam
        if len(set(arr)) == 1 and len(arr) != 1:
            return list(set(arr))

        slow = 0
        fast = 1
        for fast in range(1, len(arr) - 1):
            if arr[fast] == arr[slow]:
                fast += 1
            else:
                slow += 1
                arr[slow] = arr[fast]
                fast += 1
        slow += 1
        arr[slow] = arr[len(arr) - 1]
        return arr[:slow+1]


test_arrays = [
    [1, 1, 1],
    [1, 2, 3, 4],
    [1, 1, 1, 2, 3, 4, 5],
    [1],
    [],
    [2121221112, 2121221112, 2121221112, 2121221112]
]

for arr in test_arrays:
    print('Input: {0}'.format(arr))
    uniq_ele_arr = Solution().removeDuplicates(arr)
    print('Output: {0}'.format(uniq_ele_arr))
    print('='*20)
