"""
Problem: 2859. Sum of Values at Indices With K Set Bits
Category: Hash Map / Greedy / Bit Manipulation / Strings / Math / Arrays / Two Pointers

Description: You are given a 0-indexed integer array nums and an integer k.

Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits in their binary representation.

Algorithm:

- Iterate over every index
- Count number of set bits (with bit_count() with is available since Python 3.10+ and is more efficient)
- If number of set bits is equal to k:
    - add number in that position to the sum

Complexity:
- Time: O(n)    # Iterate over every item (bit_count can be O(1) or O(nlogW) W -> number of bits)
- Space: O(1)   # Not using extra variables

"""

class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        return sum(nums[i] if i.bit_count() == k else 0 for i in range(len(nums)))