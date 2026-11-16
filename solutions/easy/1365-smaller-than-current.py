"""
Problem: 1365. How Many Numbers Are Smaller Than the Current Number
Category: Hash Map / Arrays / Sorting

Description: Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Algorithm:

- Sort numbers in ascending order
- The position of each number tells how many numbers are smaller than itself
- From this statement, create a dictionary, where the number is the key, and the position (a.k.a. the number of smaller numbers) as the value
- Generate the final array by iterating over the original list

Complexity:
- Time: O(nlog(n))  # not having to check the same numbers multiple times
- Space: O(n)       # creating a dictionary that can be at maximum the same size as the original list

"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        d = {}
        for i, n in enumerate(sorted_nums):
            if n not in d:
                d[n] = i
        return [d[n] for n in nums]