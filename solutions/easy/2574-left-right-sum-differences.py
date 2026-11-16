"""
Problem: 2574. Left and Right Sum Differences
Category: Arrays / Prefix Sum

Description: Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:
             answer.length == nums.length and answer[i] = |leftSum[i] - rightSum[i]|.

Algorithm:

- Prepare array to make allocations faster
- Calculate the first difference with the starting pointers
- Iterate over the list, incrementing the left pointer and decrementing the right pointer and adding the new difference to the solution

Complexity:
- Time: O(n)    # iteration over the list
- Space: O(n)   # creation of a list of the same size

"""
class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        """
        One liner
        return [ abs( sum(nums[:i]) - sum(nums[i+1:])) for i in range(len(nums))]
        """
        left_sum = 0
        right_sum = sum(nums) - nums[0]
        ans = [0] * (len(nums))

        ans[0] = abs( left_sum - right_sum )

        for i in range(1, len(nums)):
            left_sum += nums[i-1]
            right_sum -= nums[i]
            print(f"{left_sum} {right_sum}")
            ans[i] = abs( left_sum - right_sum )
        
        return ans