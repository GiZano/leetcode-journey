"""
Problem: 1920. Build Array from Permutation
Category: Arrays 

Description: Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

Algorithm:

- Iterate over the items of the array
- Return a list where we add every time nums[i], where i is actually the number in the ith position

Complexity:
- Time: O(n)    # Iteration over the whole array
- Space: O(n)   # Creation of a new array with the same length

"""

class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[i] for i in nums]