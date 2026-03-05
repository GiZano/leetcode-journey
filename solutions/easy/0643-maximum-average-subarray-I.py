"""
Problem: 643. Maximum Average Subarray I
Category: Arrays / Sliding Window

Description: You are given an integer array nums consisting of n elements, and an integer k.
             Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.

Algorithm:

- Calculate the sum of the first window
- Iterate over each value starting from the right of the first window
- Calculate the new sum by adding the new value and removing the value in position [i - k]
- Keep the max total
- Return the max total divided by k 

Complexity:
- Time: O(n)    # Iterate over the list once
- Space: O(1)   # Only use integer variables

"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_total = sum(nums[:k])
        total = max_total

        for i in range(k, len(nums)):
            total = total - nums[i - k] + nums[i]
            max_total = max(max_total, total)

        return max_total/k