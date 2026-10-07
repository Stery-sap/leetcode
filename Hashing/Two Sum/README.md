# Two Sum

- **LeetCode:** [#1 - Two Sum](https://leetcode.com/problems/two-sum/)
- **Pattern:** Hashing
- **Difficulty:** Easy
- **Language:** Python

## Problem

Given an array of integers `nums` and an integer `target`, return the
indices of the two numbers such that they add up to `target`.

Each input has exactly one solution, and the same element cannot be used twice.

## Approach

Use a hash map to store numbers that have already been visited along
with their indices.

For each number:

1. Calculate its complement:
   `complement = target - num`
2. Check whether the complement already exists in the hash map.
3. If it exists, return the stored index and current index.
4. Otherwise, store the current number and its index.

This allows us to find the required pair in a single pass.

## Complexity

- **Time:** O(n)
- **Space:** O(n)

## Solution

[View solution](./solution.py)

## Detailed Explanation

Coming soon.


**Medium:** Not published yet.
