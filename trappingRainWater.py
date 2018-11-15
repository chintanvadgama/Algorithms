# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!


# Solution: Two pointer Approach
# Keep track of left maximum, right maximum and water
class Solution:
    def findTrappingWater(self,height):
        leftMax = rightMax = water = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                leftMax += max(leftMax,height[left])
                water += leftMax - height[left]
                

