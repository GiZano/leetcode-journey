"""
Problem: 1431. Kids With the Greatest Number of Candies
Category: Arrays

Description: check which kids would have the greatest number of candies if given a determined quantity of candies (extraCandies)

Algorithm:

- get the starting maximum number of candies in the group
- for each kid, check if his number of candies plus the extra would be greater than the maximum we already found
- store all data inside the "greater" list

Complexity:
- Time:  O(n)   # iterating over every kid
- Space: O(n)   # based on number of kids (candies)

"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [kid + extraCandies >= max_candies for kid in candies]