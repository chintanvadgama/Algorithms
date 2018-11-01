class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        hi = len(nums) - 1
        result = []
        for i in range(len(nums)):
            # print nums[i]
            duplicateExists = self.search(nums,i+1,hi,nums[i])
            if not duplicateExists:
                result.append(nums[i])
        return result

    def search(self,arr,l,r,target):
        found = False
        # print arr
        while l <= r and not found:
            mid = (l + r) // 2
            # print 'arr[%s]=%s, arr[%s]=%s' %(l,arr[l],r,arr[r])
            if arr[mid] == target:
                found = True
            else:
                if target < arr[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return found

print Solution().removeDuplicates([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,22,22])



class Solution2(object):
    def removeDuplicates(self, nums):
        lookup = {}
        result = []
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        if len(set(nums)) == 1 and len(nums) != 1:
            result.append(nums[0])
            return result

        for num in nums:
            if num in lookup:
                pass
            else:
                lookup[num] = 1
                result.append(num)

        return nums

print Solution2().removeDuplicates([1,1,2])

class Solution3(object):
    #In-place
    def removeDuplicates(self,nums):
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        low = 0
        high = len(nums) - 1
        index = 1
        for i in range(low,high):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        return nums



print Solution3().removeDuplicates([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,22,22])


