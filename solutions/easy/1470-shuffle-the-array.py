"""
Problem: 1470. Shuffle the Array
Category: Arrays / Two Pointers

Description: Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Algorithm:

- Iterate over every item in the list
- Using two pointers (i and i + n), add every item

Complexity:
- Time: O(n)    # iterating over every item in the list
- Space: O(n)   # creating a new array as big as the original

"""

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        ans = []
        i = 0
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
