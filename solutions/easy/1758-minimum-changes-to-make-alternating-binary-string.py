"""
Problem: 1758. Minimum Changes To Make Alternating Binary String
Category: Strings / Math / Greedy

Description: You are given a string s consisting only of the characters '0' and '1'. In one operation, 
             you can change any '0' to '1' or vice versa. 
             The string is called alternating if no two adjacent characters are equal. 
             Return the minimum number of operations needed to make s alternating.

Algorithm:

- Count whenever the string doesn't corrispond to the alternated '01010..'
- Len(s) - count represents the same count but for the string '10101...'
- Return the minimum between the two counts.

Complexity:
- Time: O(N)    # Iterating over the string once
- Space: O(1)   # Only using one integer variable

"""

class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if ((i % 2 == 0 and s[i] == '1') or (i % 2 != 0 and s[i] == '0')):
                count  += 1
        
        return min(count, len(s) - count)