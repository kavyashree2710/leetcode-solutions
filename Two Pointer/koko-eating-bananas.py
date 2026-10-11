# Problem: Kids With the Greatest Number of Candies
# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Pattern: Array Traversal
# Concepts: Lists, max(), for loop, if-else, Boolean values
# Time Complexity: O(n)
# Space Complexity: O(n), including the output list
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n=len(piles)
        def calc_time(k):
            t=0
            for i in range(n):
                if piles[i]<=k:
                    t+=1
                else:
                    t+=(piles[i]+k-1)//k
            return t
        
        left,right=1,max(piles)
        while left<=right:
            mid=(left+right)//2
            answer=calc_time(mid)
            if answer<=h:
                right=mid-1
            else:
                left=mid+1
        return left
