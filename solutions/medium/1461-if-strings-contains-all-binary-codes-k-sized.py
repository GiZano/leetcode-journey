"""
Problem: 1461. Check If a String Contains All Binary Codes of Size K
Category: Hash Table / Strings / Sliding Window / Bit Manipulation

Description: Given a binary string s and an integer k, return true if every binary code 
             of length k is a substring of s. Otherwise, return false.

Algorithm:

- If the length is too little to contain all possible codes, return False
- Use a sliding window to check every k-sized piece of string
- Save every distinct bit combination in a set
- Check if the set contains the correct amount of configurations for it to contain all possible configurations

Complexity:
- Time: O(n * k)    # N -> length of the string, to slice a string k sized, it takes O(k)
- Space: O(2^k * k) # for the set made of a maximum of 2^k strings of k length

"""

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) - k + 1 < 1 << k:
            return False
        
        binaries = set()

        for i in range(len(s) - k + 1):
            binaries.add(s[i:i+k])
        
        return len(binaries) == 1 << k