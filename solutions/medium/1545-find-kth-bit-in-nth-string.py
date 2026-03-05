"""
Problem: 1545. Find Kth Bit in Nth Binary String
Category: Strings

Description: Given two positive integers n and k, the binary string Sn is formed as follows:
             - S1 = "0"
             - Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1
             Where invert(x) inverts all bits and reverse(x) reverses the string.
             Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

Algorithm:

- Find the Nth string by iterating:
    - start from '0'
    - get the invert all bits
    - create the new Nth string (previous string + '1' + the invert but reversed)

Complexity:
- Time: O(2^n)  # We have to calculate a string that doubles every step
- Space: O(2^n) # We have to store a string of length 2^n -1

"""

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'

        for i in range(n-1):
            inverted = ''.join('1' if bit == '0' else '0' for bit in s)
            s = s + '1' + inverted[::-1]

        return s[k-1]