# Problem: Merge Strings Alternately
# Link: https://leetcode.com/problems/merge-strings-alternately/
# Pattern: Two Pointers
# Concepts: Strings, Indexing, while loop, String Concatenation, Slicing
# Time Complexity: O(n + m), where n and m are the lengths of word1 and word2
# Space Complexity: O(n + m), including the output string

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        merged_string = ''

        while i <= len(word1) - 1 and j <= len(word2) - 1:
            merged_string = merged_string + word1[i] + word2[j]
            i += 1
            j += 1

        if i <= len(word1) - 1:
            merged_string = merged_string + word1[i:]

        if j <= len(word2) - 1:
            merged_string = merged_string + word2[j:]

        return merged_string