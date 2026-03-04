"""
Problem: 392. Is Subsequence
Category: Strings / Two Pointers

Description: Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
             A subsequence of a string is a new string that is formed from the original string by deleting some 
             (can be none) of the characters without disturbing the relative positions of the remaining characters.

Algorithm:

- Define two pointers, one per string
- Iterate over t:
    - If the current char of s is the same, increment the s pointer
- If the s pointer has reached the same value as the length of s, it means we found the subsequence

Complexity:
- Time: O(n)    # traveling through the strings once
- Space: O(1)   # creating two integer variables

"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pos_t = 0
        pos_s = 0

        while pos_s < len(s) and pos_t < len(t):
            if s[pos_s] == t[pos_t]:
                pos_s += 1
            pos_t += 1
        
        return pos_s == len(s)