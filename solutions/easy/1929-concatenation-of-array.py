"""
Problem: 1929. Concatenation of Array
Category: Arrays

Description: Create an array of size 2n, made by the concatenation of the same array

Algorithm:

- Return the sum of the two arrays

Complexity:
- Time: O(n)    # Iteration over the whole list twice (2n)
- Space: O(n)   # Creation of a new array that is twice the original one (2n)

"""

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums
