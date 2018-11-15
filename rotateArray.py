
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            last_element = nums.pop()
            nums.insert(0, last_element)
        return nums

    def rotate2(self, nums, k):
        nums.reverse()
        list1, list2 = nums[:k], nums[k:]
        list1.reverse()
        list2.reverse()
        return list1 + list2
        # Using Reverse
        # [1,2,3,4,5] => [5,4,3,2,1]
        # Rotate by 3


print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3))
