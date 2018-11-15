class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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


class Solution2(object):
    def removeDuplicates(self,nums):
        if len(nums) == 1:
            return nums
        if len(set(nums)) == 1:
            return list(set(nums))
        low = 0
        hi = len(nums) - 1
        swapped = 1
        for i in range(low,hi):
            if nums[i-1] < nums[i]:
                nums[i],nums[i-1] = nums[i-1],nums[i]
        return nums

class SetSolution(object):
    def removeDuplicates(self,nums):
        if len(nums) == 1:
            return nums
        if len(set(nums)) == 1 and len(nums) != 1:
            return list(set(nums))
        lookup = set()
        for num in nums:
            if num not in lookup:
                lookup.add(num)

        return list(lookup)


print(SetSolution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))