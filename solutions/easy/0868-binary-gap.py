"""
Problem: 868. Binary Gap
Category: Bit Manipulation / Strings 

Description: Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. 
             If there are no two adjacent 1's, return 0.

Algorithm:

- Get the binary representation
- Check every bit
- If 0:
    - Count up
- If 1:
    - Check if a new maximum has been found and save it
    - reset count to 1

Complexity:
- Time: O(log n)    # binary representation is proportional to log n
- Space: O(log n)   # based on binary representation of the number

"""

class Solution:
    def binaryGap(self, n: int) -> int:
        count = 0
        max_count = 0
        n_bin = bin(n)
        if n.bit_count() == 1:
            return 0
        for bit in n_bin[2:]:
            if bit == '0':
                count += 1
            else:
                max_count = max(count, max_count)
                count = 1
        return max_count