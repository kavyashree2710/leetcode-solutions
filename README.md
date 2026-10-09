<div align="center">

# 🧠 DSA Pattern Practice

### 100 Days · Pattern by Pattern · Python

![Challenge](https://img.shields.io/badge/Challenge-100%20Days-2A6F77?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-5%20%2F%20100-F2A900?style=for-the-badge)
![Solved](https://img.shields.io/badge/Solved-9-3C6E47?style=for-the-badge)
![Language](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)

`█░░░░░░░░░░░░░░░░░░░` **5%**

</div>

---

## 📑 Contents
- [How I Study](#-how-i-study)
- [Roadmap](#-roadmap)
- [Pattern Progress](#-pattern-progress)
- [Solved Problems](#-solved-problems)
- [Daily Log](#-daily-log)
- [Pattern Notes](#-pattern-notes)
- [Mistakes Log](#-mistakes-log)
- [Repo Structure](#-repo-structure)

---

## 🎯 How I Study

| Rule | Details |
|---|---|
| **Weekly rhythm** | 5 days of new problems, 2 days of revision |
| **Cumulative revision** | 3 extra days after every 4 weeks (days 29-31, 60-62, 91-93) |
| **Attempt first** | At least 25 minutes of my own attempt before any hint |
| **Trace by hand** | Dry-run an example before submitting |
| **Notes per pattern** | Trigger signs, template, and mistakes |
| **Final week** | Mixed problems with hidden patterns, plus a timed mock |

---

## 🗺️ Roadmap

| Week | Patterns | Status |
|---|---|---|
| 1 | Two Pointers + Binary Search | 🟡 In progress |
| 2 | Sliding Window + Fast & Slow Pointers | ⚪ |
| 3 | Prefix Sum + Merge Intervals | ⚪ |
| 4 | Linked List Manipulation | ⚪ |
| 🔁 | Cumulative revision (Weeks 1-4) | ⚪ |
| 5 | Backtracking | ⚪ |
| 6 | Trees: DFS / BFS | ⚪ |
| 7 | Graphs: BFS / DFS | ⚪ |
| 8 | Topological Sort + Union-Find | ⚪ |
| 🔁 | Cumulative revision (Weeks 5-8) | ⚪ |
| 9 | Greedy | ⚪ |
| 10 | Dynamic Programming: 1D | ⚪ |
| 11 | Dynamic Programming: 2D | ⚪ |
| 12 | Heaps, Trie, Monotonic Stack, Bit Manipulation | ⚪ |
| 🔁 | Cumulative revision (Weeks 9-12) | ⚪ |
| 🏁 | Final week: mixed practice and mock contest | ⚪ |

---

## 📊 Pattern Progress

| Pattern | Status | Solved |
|---|---|---|
| Two Pointers | 🟡 In progress | 5 / 6 |
| Binary Search | 🟡 In progress | 4 / 5 |
| Sliding Window | ⚪ Not started | 0 / 6 |
| Fast & Slow Pointers | ⚪ Not started | 0 / 5 |

---

## ✅ Solved Problems

### Two Pointers

| # | Problem | Difficulty | Time | Space | Code |
|---|---|---|---|---|---|
| 167 | [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | 🟠 Medium | O(n) | O(1) | [🔗](Two%20Pointer/two-sum-ii.py) |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | 🟢 Easy | O(n) | O(1) | [🔗](Two%20Pointer/valid-palindrome.py) |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 🟠 Medium | O(n) | O(1) | [🔗](Two%20Pointer/container-with-most-water.py) |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | 🟠 Medium | O(n²) | O(1) | [🔗](Two%20Pointer/3sum.py) |
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | 🟢 Easy | O(n) | O(1) | [🔗](Two%20Pointer/remove-duplicates-from-sorted-array.py) |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | 🔴 Hard | - | - | ⏳ Pending |

### Binary Search

| # | Problem | Difficulty | Time | Space | Code |
|---|---|---|---|---|---|
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | 🟢 Easy | O(log n) | O(1) | [🔗](Binary%20Search/binary-search.py) |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | 🟠 Medium | O(log n) | O(1) | [🔗](Binary%20Search/search-in-rotated-sorted-array.py) |
| 34 | [First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | 🟠 Medium | O(log n) | O(1) | [🔗](Binary%20Search/find-first-and-last-position.py) |
| 875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | 🟠 Medium | O(n log m) | O(1) | [🔗](Binary%20Search/koko-eating-bananas.py) |
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 🔴 Hard | - | - | ⏳ In progress |

---

## 📅 Daily Log

| Day | Focus | Problems | Status |
|---|---|---|---|
| 1 | Two Pointers | Two Sum II, Valid Palindrome, Container With Most Water | ✅ |
| 2 | Two Pointers | 3Sum, Remove Duplicates from Sorted Array | ✅ |
| 3 | Binary Search | Binary Search, Search in Rotated Sorted Array | ✅ |
| 4 | Binary Search | First and Last Position, Koko Eating Bananas | ✅ |
| 5 | Stretch (Hard) | Median of Two Sorted Arrays, Trapping Rain Water | 🟡 |

---

## 📝 Pattern Notes

<details>
<summary><b>Two Pointers</b></summary>

- **Trigger signs:** sorted array with a pair or target, palindrome checks, maximizing something between two endpoints, in-place duplicate removal.
- **Converging pointers** (start at both ends, move inward): Two Sum II, Valid Palindrome, Container With Most Water, 3Sum.
- **Read/write pointers** (both move left to right, one scans and one marks the write position): Remove Duplicates.
- **Container insight:** always move the pointer on the limiting side, because moving the taller one can never improve the area.
- **3Sum:** sort first, fix one number, run two pointers on the rest, and skip duplicates on all three positions.
- **Template:** `left, right = 0, n - 1`, then `while left < right`, and move a pointer based on a condition.

</details>

<details>
<summary><b>Binary Search</b></summary>

- **Trigger signs:** sorted or rotated array, searching for a value, a boundary, or a range of possible answers.
- **Rotated array:** one half is always sorted. Compare `nums[left]` to `nums[mid]` to find it, then check whether the target lies in that half.
- **Boundaries (first/last occurrence):** don't stop at the first match. Keep narrowing toward the side you need, using two separate binary searches. Expanding outward from one match breaks O(log n).
- **Binary search on the answer (Koko):** search over a range of possible answers with a helper that checks whether a guess is good enough. Use `<=`, not `==`, because the check value can skip numbers. Return `left` after the loop.

</details>

---

## 🐞 Mistakes Log

<details>
<summary><b>Open the log</b></summary>

| Problem | Mistake | Lesson |
|---|---|---|
| Two Sum II | Missing `return` on a match, mixed `for` with `while`, forgot 1-indexing | Return immediately on a match, and re-read "indexed" wording |
| Valid Palindrome | Used `if` where `while` was needed to skip characters | Skipping until a condition is met needs `while` |
| 3Sum | Loop started at index 1, and duplicate skipping compared the wrong neighbor | Check `left-1` / `right+1`, and trace `[0,0,0,0]` |
| Search in Rotated Array | `<` vs `<=` on the inclusive boundary | The inclusive side depends on which end of the sorted half `mid` sits at |
| First/Last Position | Linear expand-outward from one match (crash risk and O(n)) | Use two boundary binary searches |
| Koko Eating Bananas | Searched for `== h`, returned hours instead of speed | Use `<= h` and return the speed |

**Recurring theme:** boundary conditions (`<` vs `<=`, `==` vs `<=`, off-by-one). Fix: trace an example by hand before submitting.

</details>

---

## 📂 Repo Structure

```
leetcode-solutions/
├── Two Pointer/
│   ├── two-sum-ii.py
│   ├── valid-palindrome.py
│   ├── container-with-most-water.py
│   ├── 3sum.py
│   └── remove-duplicates-from-sorted-array.py
├── Binary Search/
│   ├── binary-search.py
│   ├── search-in-rotated-sorted-array.py
│   ├── find-first-and-last-position.py
│   └── koko-eating-bananas.py
└── README.md
```

---

## 🎯 Up Next
- [ ] Finish Day 5: Median of Two Sorted Arrays, Trapping Rain Water
- [ ] Week 1 revision days: redo the hardest problems without hints
- [ ] Week 2: Sliding Window + Fast & Slow Pointers