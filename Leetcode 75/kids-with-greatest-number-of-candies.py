# Problem: Kids With the Greatest Number of Candies
# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Pattern: Array Traversal
# Concepts: Lists, max(), for loop, if-else, Boolean values
# Time Complexity: O(n)
# Space Complexity: O(n), including the output list
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        greatest=max(candies)
        result=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=greatest:
                result.append(True)
            else:
                result.append(False)
        return result