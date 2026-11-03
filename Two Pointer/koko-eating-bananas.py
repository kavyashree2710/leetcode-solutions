# Problem: Koko Eating Bananas
# Link: https://leetcode.com/problems/koko-eating-bananas/
# Pattern: Binary Search (binary search on the answer)
# Time Complexity: O(n log m), m = max(piles)
# Space Complexity: O(1)
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
