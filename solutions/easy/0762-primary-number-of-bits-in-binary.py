"""
Problem: 762. Prime Number of Set Bits in Binary Representation
Category: Bit Manipulation / Math 

Description: Given two integers left and right, return the count of numbers in the 
             inclusive range [left, right] having a prime number of set bits in their binary representation.

Algorithm:

- The maximum number of bits in numbers up to 10^6 is 32
- Create a list or dict with all available primes from 2 to 31
- For every number, get the number of set bits with bit_count and check if the value is inside the created list
- Sum the number of found answers

Complexity:
- Time: O(n)    # Checking all numbers from left to right
- Space: O(1)   # Creating a list with fixed length for primes (11)

"""

class Solution:      

    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}

        return sum(num.bit_count() in primes for num in range(left, right+1))