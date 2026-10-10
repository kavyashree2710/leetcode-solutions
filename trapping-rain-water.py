# Problem: Trapping Rain Water
# Link: https://leetcode.com/problems/trapping-rain-water/
# Pattern: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def trap(self, height: list[int]) -> int:
       left,right=0,len(height)-1
       max_left,max_right=0,0
       water_unit=0

       while left<right:
            if height[left]<=height[right]:
                if height[left]>=max_left:
                    max_left=height[left]
                else:
                    water_unit+=max_left-height[left]
                left+=1
            else:
                if height[right]>=max_right:
                    max_right=height[right]
                else:
                    water_unit+=max_right-height[right]
                right-=1
       return water_unit
