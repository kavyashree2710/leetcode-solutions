# Problem: 3Sum
# Link: https://leetcode.com/problems/3sum/
# Pattern: Two Pointers
# Time Complexity: O(n^2)
# Space Complexity: O(1) extra (excluding output)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result= []
        n=len(nums)

        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue

            left,right=i+1,n-1

            while left<right:
                total=nums[i]+nums[left]+nums[right]

                if total==0:
                    result.append([nums[i],nums[left],nums[right]])

                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
        return result
