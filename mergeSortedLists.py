class Solution(object):
    def merge(self, nums1, nums2):
        """
        Space O(m+n)

        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        n1 = len(nums1)
        n2 = len(nums2)
        merged_list = [None] * (n1+n2)
        i = 0
        j = 0
        k = 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                if merged_list[k-1] != nums1[i]:
                    merged_list[k] = nums1[i]
                    i += 1
                    k += 1
            else:
                if merged_list[k-1] != nums2[j]:
                    merged_list[k] = nums2[j]
                    j += 1
                    k += 1

        while i < n1:
            if merged_list[k-1] != nums1[i]:
                merged_list[k] = nums1[i]
                k += 1
                i += 1

        while j < n2:
            if merged_list[k-1] != nums2[j]:
                merged_list[k] = nums2[j]
                k += 1
                j += 1

        return merged_list

print(Solution().merge([1,2,3,4],[2,3,4]))
