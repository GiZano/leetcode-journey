"""
Problem: 11. Container With Most Water
Category: Arrays / Two Pointers / Greedy

Description: You are given an integer array height of length n. There are n vertical lines drawn such that 
             the two endpoints of the ith line are (i, 0) and (i, height[i]).
             Find two lines that together with the x-axis form a container, such that the container contains the most water.
             Return the maximum amount of water a container can store.

Algorithm:

- Define two pointers, one at the start and the other at the end, and a variable to store the maximum found water
- Iterate using the two pointers:
    - If a new greatest water is found, store it
    - If the height of the line pointed by start is greater, decrement the end pointer
    - Else increment the start pointer
- Return the maximum found water

Complexity:
- Time: O(n)    # Iterate over the list once
- Space: O(1)   # Only use three integer variables

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        water = 0

        while start < end:
            water = max(water, (min(height[start], height[end])*(end-start)))
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return water