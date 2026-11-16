"""
Problem: 1720. Decode XORed Array
Category: Bit Manipulation / Arrays

Description: There is a hidden integer array arr that consists of n non-negative integers.
             It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].
             You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].
             Return the original array arr. It can be proved that the answer exists and is unique.

Algorithm:

- Prepare the final array size to make allocations quicker
- Iterate over the encoded array
- Reverse XOR the array to find the original one

Complexity:
- Time: O(n)    # iteration over the list
- Space: O(n)   # creating a new list of the same size as the given one (n+1)

"""

class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        arr = [0] * (len(encoded) + 1)
        arr[0] = first

        for i in range(1, len(arr)):
            arr[i] = arr[i-1] ^ encoded[i-1]
        
        return arr