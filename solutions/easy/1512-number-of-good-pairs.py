"""
Problem: 1512. Number of Good Pairs
Category: Arrays

Description: Given an array of integers nums, return the number of good pairs.

Algorithm:

- Iterate over the array with two pointers (one starting from 0 {i}, and one starting from i + 1 {j})
- Increment if the condition is met (nums[i] == nums[j])
- (i is natively less than j as j always starts from i+1)

Complexity:
- Time: O(n^2)  # iterating over all the items almost n times (actually time is a bit less)
- Space: O(1)   # no extra variables used to store pairs

"""

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        return sum(nums[i] == nums[j] for i in range(len(nums)-1) for j in range(i+1, len(nums)))