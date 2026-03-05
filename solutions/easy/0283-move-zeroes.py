"""
Problem: 283. Move Zeroes
Category: Arrays / Two Pointers

Description: Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
             Note that you must do this in-place without making a copy of the array.

Algorithm:

- Create two variables, read and write
- Iterate through the array
    - If a non-zero number is found, write it in the 'write' position and increment the write pointer
    - Else increment the read pointer
- After that iterate from the current write to the last position and set all values as 0

Complexity:
- Time: O(N)    # Iterate the array once
- Space: O(1)   # Only use pointer variables

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read = 0
        write = 0

        while read < len(nums):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
            read += 1
        
        while write < len(nums):
            nums[write] = 0
            write += 1