"""
Problem: 696 Count Binary Substrings

Description: Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Algorithm:

- Start checking every bit and count
- When the bit changes:
    - add to output the minimum value between actual count and last count
    - set countBefore as actual count
    - reset countNow 
- After the whole check, add to out the last minimum between countNow and countBefore
- Return out

Complexity:
- Time: O(n)    # scanning once the whole string
- Space: O(1)   # using only three integer variables

"""
class Solution:    
    def countBinarySubstrings(self, s: str) -> int:
        countBefore = 0
        countNow = 1
        out = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                out += min(countBefore, countNow)
                countBefore = countNow
                countNow = 1
            else:
                countNow += 1
        out += min(countBefore, countNow)
        return out
