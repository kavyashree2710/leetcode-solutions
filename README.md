# DSA Practice - 100 Day Challenge

Tracking my progress learning data structures & algorithms, pattern by pattern.

## Progress Log

### Day 1 - Two Pointers
- [x] Two Sum II (sorted array)
- [x] Valid Palindrome
- [x] Container With Most Water

### Day 2 - Two Pointers
- [x] 3Sum
- [x] Remove Duplicates from Sorted Array

### Day 3 - Binary Search
- [x] Binary Search
- [x] Search in Rotated Sorted Array

### Day 4 - Binary Search
- [x] Find First and Last Position of Element in Sorted Array
- [x] Koko Eating Bananas

## Notes

**Two Pointers**
- Trigger signs: sorted array + pair/target, palindrome checks, maximizing area between two endpoints, in-place duplicate removal
- Two flavors seen so far:
  - Converging pointers (start at both ends, move toward each other) — Two Sum II, Valid Palindrome, Container With Most Water, 3Sum
  - Read/write pointers (both move left to right, one marks position, one scans) — Remove Duplicates from Sorted Array
- Common mistakes I made: forgetting to `return` on a match, mixing `for`/`while`, using `if` instead of `while` when skipping multiple characters, wrong direction when skipping duplicates (comparing to the wrong neighbor index)

**Binary Search**
- Trigger signs: sorted (or rotated) array, searching for a value, a boundary, or a range of possible answers
- Rotated array search: figure out which half is sorted first (compare `nums[left]` to `nums[mid]`), then check if target falls in that half's range before deciding where to search
- Boundary-finding (first/last occurrence): don't stop at the first match — keep narrowing in the direction you need (left for first occurrence, right for last) using two separate binary searches, not a linear expand-outward scan (that breaks the O(log n) requirement)
- Mistake I made: off-by-one in inclusive/exclusive range checks (`<=` vs `<`) when deciding which sorted half contains the target