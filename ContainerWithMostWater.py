# The idea is to keep track of area and find max area using two pointers
class Solution:
    def maxArea(self, height):
        first = 0
        last = len(height) - 1
        water = 0
        while first < last:
            area = (last - first) * min(height[last], height[first])
            water = max(area, water)
            if height[first] < height[last]:
                first += 1
            else:
                last -= 1
        return water






