# Problem: Reverse Vowels of a String
# Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
# Pattern: Two Pointers
# Concepts: Strings, Lists, Two Pointers, While Loop, Conditional Statements, Swapping, String Conversion
# Time Complexity: O(n)
# Space Complexity: O(n), due to converting the string into a list

class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        s = list(s)

        while left < right:
            while left < right and s[left] not in "aeiouAEIOU":
                left += 1

            while left < right and s[right] not in "aeiouAEIOU":
                right -= 1

            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)