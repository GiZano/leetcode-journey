"""
Problem: 1389. Create Target Array in the Given Order
Category: Arrays

Description: [Explain the problem]

Algorithm:

- Iterate over every item
- Insert at index[i] the value nums[i]

Complexity:
- Time: O(n^2)  # insert causes the array to be interated again every time
- Space: O(n)   # we create a new array {ans} as big as the given ones

"""

class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        ans = []
        for i in range(len(index)):
            ans.insert(index[i], nums[i])
        return ans