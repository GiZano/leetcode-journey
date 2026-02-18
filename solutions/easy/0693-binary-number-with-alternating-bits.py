"""
Problem: 0693 Binary Number With Alternating Bits

Description: Check if a number binary version is formed by only alternating bits (i.e. '101', '010')

Algorithm:

- Create a second number with bits moved to the right by one (i.e. n = 101, x=010)
- XOR the new number and the original one (101 ^ 010 = 111)
    (XOR -> 1 if different, 0 if equal)
- Check if all digits are one 
    - 010 & 011 = 0 (they aren't the same number)

Complexity:
- Time:  O(1)   # No need to iterate over values
- Space: O(n)   # Creating a new number starting from the given one

"""

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n >> 1
        x = x ^ n
        if x & (x+1) == 0:
            return True
        return False