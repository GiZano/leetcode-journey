"""
Problem: 1071 Greatest Common Divisor of Strings

Description: find the greatest common divisor of two given strings (str1, str2)

Algorithm:

- check if both strings are formed by the same sub-strings (str1 + str2 == str2 + str1)
- get gcd of string lengths using math lib
- get the first {gcd} characters of any of the two strings to find the string gcd.

Complexity:
- Time:  O(n + m)   # '==' operation and str1 + str2 concatenation (picking every single char)
- Space: O(n + m)   # str1 + str2 operation

"""

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        
        gcd = math.gcd(len(str1), len(str2))

        return str1[:gcd]

