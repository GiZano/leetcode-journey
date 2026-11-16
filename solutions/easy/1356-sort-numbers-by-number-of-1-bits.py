"""
Problem: 1356. Sort Integers by The Number of 1 Bits
Category: Bit Manipulation / Arrays

Description: Given an integer array, sort items by number of 1 bits. 
             If two numbers have the same number of active bits, sort them by actual number (asc).

Algorithm:

- Create a lambda (comparing every value and creating the final dict at the end)
- Use two conditions:
    - number of active bits
    - actual number

Complexity:
- Time: O(n)    # Check every position (key, value)
- Space: O(n)   # Creation of tuples for every position

"""

class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        return sorted(arr, key=lambda x: (x.bit_count(), x))
