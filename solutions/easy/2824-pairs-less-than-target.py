"""
Problem: 2824. Count Pairs Whose Sum is Less than Target
Category: Arrays / Two Pointers / Sorting

Description: Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.

Algorithm:

- Create two pointers, one at the start and one at the end
- Sort the original list
- Iterate until left is greater or equal to right
- If the sum of numbers on the left-th and the right-th positions are less than target:
    - add the right - left found solutions (as they are in ascending order, all values from left to right will be acceptable)
    - 

Complexity:
- Time: O(nlog(n))  # cutting off many checks when the conditions is met
- Space: O(1)       # using only integer variables

"""

class Solution:
    """
    One liner: (Time O(n^2), Space: O(1))

    def countPairs(self, nums: List[int], target: int) -> int:
        return sum(nums[i] + nums[j] < target for i in range(len(nums)-1) for j in range(i+1, len(nums)))
    """

    def countPairs(self, nums: list[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        out = 0
        while left < right:
            if nums[left] + nums[right] < target:
                out += right - left
                left += 1
            else:
                right -=1
        return out