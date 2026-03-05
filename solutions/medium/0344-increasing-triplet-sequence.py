"""
Problem: 334. Increasing Triplet Subsequence
Category: Greedy / Arrays

Description: Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
             such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exist, return false.

Algorithm:

- Create two pointing variables, initialized as infinite so each number will be below it
- Iterate over each number:
    - If it is lower than the first, save it as the first 'guardian'
    - Else if it is lower than the second, save it as the second 'guardian'
    - Finally, if it wasn't lower than other two, we found the final number of the sequence and we can return true
- If the third hasn't been found, return false

Complexity:
- Time: O(n)    # Iterate over each number once
- Space: O(1)   # Using only two int variables

"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = float('inf')
        b = float('inf')

        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        return False
        