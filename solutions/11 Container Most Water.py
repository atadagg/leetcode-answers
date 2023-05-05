#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

#Find two lines that together with the x-axis form a container, such that the container contains the most water.

#Return the maximum amount of water a container can store.


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            current_area = min(height[right], height[left]) * (right - left)
            max_area = max(current_area, max_area)
            if height[left]>height[right]:
                right -= 1
            else:
                left += 1
        return max_area
