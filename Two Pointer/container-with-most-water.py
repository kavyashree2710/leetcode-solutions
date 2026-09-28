# Problem: Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/
# Pattern: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left,right=0,len(height)-1
        max_area=0
        min_height=0
        while left<right:
            dif=right-left
            min_height=min(height[left],height[right])
            max_area=max(max_area,min_height*dif)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area