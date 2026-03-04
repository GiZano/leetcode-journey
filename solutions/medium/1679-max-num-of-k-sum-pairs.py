"""
Problem: 1679. Max Number of K-Sum Pairs
Category: Arrays / Two Pointers

Description: You are given an integer array nums and an integer k.
             In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
             Return the maximum number of operations you can perform on the array.

Algorithm:

- Sort the list
- Define the pointer variables and a counter
- Get the sum of the pointed values
- If it equals k, decrement the end, increment the start and count the found couple
- If it is greater, decrement the end
- If it is less, increment the start

Complexity:
- Time: O(nlogn) # time to sort (iterating is then n)
- Space: O(1)    # Only use integer variables

"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        end = len(nums)-1
        count = 0
        
        while start < end:
            tot = nums[start] + nums[end]
            if tot == k:
                count += 1
                start += 1
                end -= 1
            elif tot > k:
                end -= 1
            else:
                start += 1

        return count
