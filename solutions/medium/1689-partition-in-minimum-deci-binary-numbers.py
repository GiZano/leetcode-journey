"""
Problem: 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
Category: Strings / Math / Greedy

Description: A decimal number is called deci-binary if each of its digits is either 0 or 1 without 
             any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
             Given a string n that represents a positive decimal integer, return the minimum number 
             of positive deci-binary numbers needed so that they sum up to n.

Algorithm:

- Find the highest digit in the given number
- Return it as an integer

Complexity:
- Time: O(n)    # Iterate over every digit of the string
- Space: O(1)   # No new variables are used

"""

class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))