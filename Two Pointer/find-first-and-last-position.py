# Problem: Find First and Last Position of Element in Sorted Array
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Pattern: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_first():
            left,right=0,len(nums)-1
            answer=-1
            while left<=right:
                mid=(left+right)//2

                if nums[mid]==target:
                    answer=mid
                    right=mid-1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1

            return answer

        def find_last():
            left,right=0,len(nums)-1
            answer=-1
            while left<=right:
                mid=(left+right)//2

                if nums[mid]==target:
                    answer=mid
                    left=mid+1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1

            return answer

        return [find_first(),find_last()]

