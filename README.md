# DSA Practice – 100 Day Challenge

Tracking my progress learning **Data Structures & Algorithms**, pattern by pattern, with a focus on understanding the approach and improving problem-solving skills.

## Progress Log

### Day 1 – Two Pointers

* [x] Two Sum II (Sorted Array)
* [x] Valid Palindrome
* [x] Container With Most Water

### Day 2 – Two Pointers

* [x] 3Sum
* [ ] Remove Duplicates from Sorted Array

### Day 3 – Binary Search

* [x] Binary Search
* [ ] Search in Rotated Sorted Array *(attempted — finishing tomorrow)*

## Patterns & Notes

### Two Pointers

**Trigger signs:**

* Sorted array + pair/target search
* Checking whether a string/array is a palindrome
* Comparing elements from both ends
* Finding the maximum/minimum based on two endpoints

**Common mistakes I made:**

* Forgetting to `return` when a match is found
* Mixing up `for` and `while` loop logic
* Using `if` instead of `while` when skipping multiple duplicate/invalid characters
* Moving the wrong pointer without checking what the comparison requires

**Key idea:**

Use two indices and move them based on the condition instead of repeatedly scanning the array.

---

### Binary Search

**Trigger signs:**

* Sorted array
* Searching for a specific value
* Finding a boundary or position
* Rotated sorted array
* Problems where the search space can be divided in half

**Key idea:**

Instead of checking every element, repeatedly eliminate half of the search space.

**Things to remember:**

* Calculate the middle index carefully
* Decide whether to move `left` or `right` based on the comparison
* Make sure the search range actually shrinks
* Handle the final remaining element correctly
* For rotated arrays, first determine which half is sorted

**Common mistake to watch for:**

* Updating `left`/`right` incorrectly and creating an infinite loop or skipping the answer

## Goal

**100 Days → Consistent DSA Practice → Better Problem Solving**

Focus is not just on solving problems, but on recognizing patterns and understanding **why** a particular approach works.
