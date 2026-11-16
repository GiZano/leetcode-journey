"""
Problem: 1. Two Sum
Category: Hash Map

Description: Find the two numbers that add up to the target value

Algorithm:
- Start generating a dict where the key is the ith number and the value is its position (i)
- If the difference between the target number and the ith number is already in the dict
    - return the two positions (i - current number and d[target - num] - other number)

Complexity:
- Time:  O(n)   # checking at maximum all numbers
- Space: O(n)   # creating a dict as big as the original array
    
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [i, d[target - num]]
            d[num] = i