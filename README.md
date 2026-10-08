# 🧠 DSA Pattern Practice: 100 Day Challenge

![Challenge](https://img.shields.io/badge/Challenge-100%20Days-blue)
![Current Day](https://img.shields.io/badge/Current%20Day-5-orange)
![Solved](https://img.shields.io/badge/Solved-9-brightgreen)
![Language](https://img.shields.io/badge/Language-Python-yellow)

Learning data structures and algorithms **pattern by pattern**: 5 days of study and 2 days of revision each week, plus a cumulative revision block after every 4 weeks.

**Progress:** `▓▓▓▓▓░░░░░░░░░░░░░░░░░░░` Day 5 / 100

---

## 📊 Pattern Progress

| Pattern | Status | Solved |
|---|---|---|
| Two Pointers | 🟡 In progress | 5 / 6 |
| Binary Search | 🟡 In progress | 4 / 5 |
| Sliding Window | ⚪ Not started | 0 / 6 |
| Fast & Slow Pointers | ⚪ Not started | 0 / 5 |
| Prefix Sum | ⚪ Not started | 0 / 4 |
| Merge Intervals | ⚪ Not started | 0 / 4 |

---

## ✅ Solved Problems

### Two Pointers

| Problem | Difficulty | Time | Space | Solution |
|---|---|---|---|---|
| [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | O(n) | O(1) | [code](Two%20Pointer/two-sum-ii.py) |
| [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | O(n) | O(1) | [code](Two%20Pointer/valid-palindrome.py) |
| [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | O(n) | O(1) | [code](Two%20Pointer/container-with-most-water.py) |
| [3Sum](https://leetcode.com/problems/3sum/) | Medium | O(n²) | O(1) | [code](Two%20Pointer/3sum.py) |
| [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy | O(n) | O(1) | [code](Two%20Pointer/remove-duplicates-from-sorted-array.py) |
| [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard | - | - | ⏳ Pending |

### Binary Search

| Problem | Difficulty | Time | Space | Solution |
|---|---|---|---|---|
| [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | O(log n) | O(1) | [code](Binary%20Search/binary-search.py) |
| [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | O(log n) | O(1) | [code](Binary%20Search/search-in-rotated-sorted-array.py) |
| [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Medium | O(log n) | O(1) | [code](Binary%20Search/find-first-and-last-position.py) |
| [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | O(n log m) | O(1) | [code](Binary%20Search/koko-eating-bananas.py) |
| [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | - | - | ⏳ In progress |

---

## 📅 Daily Log

| Day | Pattern | Problems | Status |
|---|---|---|---|
| 1 | Two Pointers | Two Sum II, Valid Palindrome, Container With Most Water | ✅ |
| 2 | Two Pointers | 3Sum, Remove Duplicates from Sorted Array | ✅ |
| 3 | Binary Search | Binary Search, Search in Rotated Sorted Array | ✅ |
| 4 | Binary Search | Find First and Last Position, Koko Eating Bananas | ✅ |
| 5 | Stretch (Hard) | Median of Two Sorted Arrays, Trapping Rain Water | 🟡 In progress |

---

## 📝 Pattern Notes

### Two Pointers
- **Trigger signs:** sorted array with a pair/target, palindrome checks, maximizing something between two endpoints, in-place duplicate removal.
- **Flavor 1, converging pointers** (start at both ends, move inward): Two Sum II, Valid Palindrome, Container With Most Water, 3Sum.
- **Flavor 2, read/write pointers** (both move left to right, one scans and one marks the write position): Remove Duplicates.
- **Key insight (Container):** always move the pointer on the *limiting* side, because moving the taller one can never improve the result.
- **3Sum:** sort first, fix one number, run two pointers on the rest, and skip duplicates on all three positions.

### Binary Search
- **Trigger signs:** sorted or rotated array, searching for a value, a boundary, or a range of possible answers.
- **Rotated array:** one half is always sorted. Find it by comparing `nums[left]` to `nums[mid]`, then check whether the target lies in that half.
- **Boundaries (first/last occurrence):** don't stop at the first match. Keep narrowing in the direction you need, using two separate binary searches. Expanding outward from one match breaks O(log n).
- **Binary search on the answer (Koko):** search over a range of possible answers, using a helper that checks "is this guess good enough?". Use `<=`, not `==`, because the check value can skip numbers. Return `left` after the loop.

---
