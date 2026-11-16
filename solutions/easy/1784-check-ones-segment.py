"""
Problem: 1784. Check if Binary String Has at Most One Segment of Ones
Category: Strings / Arrays 

Description: Given a binary string s ​​​​​without leading zeros, 
             return true​​​ if s contains at most one contiguous segment of ones. 
             Otherwise, return false.

Algorithm:

- All strings start with '1'
- If there is the string '01', it means a new ones segment as started

Complexity:
- Time: O(N)    # Iterating over the string at most twice (split and len)
- Space: O(1)   # Not creating new variables

"""

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s