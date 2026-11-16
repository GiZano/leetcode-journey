"""
Problem: 238. Product of Array Except Self
Category: Arrays / Prefix Sum

Description: Given an integer array nums, return an array answer such that answer[i] is equal 
             to the product of all the elements of nums except nums[i].
             You must write an algorithm that runs in O(N) time and without using the division operation.
             Follow-up: Solve in O(1) extra space complexity.

Algorithm:

- Create the variables (answer with all positions to modify faster laster)
- Iterate over every element of nums, starting from the second, to calculate the 'left' products (nums from 0 to i-1)
- Iterate over every element of nums (in opposite order) and multiply each answer slot (left product) by the right product
- Multiply the right variable to remember how much was the right product before (so we don't have to iterate again over the whole array)

Complexity:
- Time: O(n)    # Iterating only two times over the array in a linea time
- Space: O(1)   # Using only the array list (not counted as LeetCode mentioned in the description)

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length
        right = 1

        for i in range(1, length):
            answer[i] = answer[i-1] * nums[i-1]
        
        for i in range(length - 1, -1, -1):
            answer[i] *= right
            right = right * nums[i]
        
        return answer