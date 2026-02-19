"""
Problem: 605. Can Place Flowers
Category: Greedy

Description: Check if it's possible to place 'n' flowers in a flowerbed, counting all space without flowers nearby

Algorithm:

- Add padding before and after list to be able to iterate over all positions correctly
- Check if place before and after are occupied
- IF NOT --> occupy new space and count up the available spaces
- IF YES --> just go on counting
- At the end of every iteration, check if the number of available spaces has reached the number of needed spaces
- If the number hasn't been reached at the end, return False

Complexity:
- Time:  O(n)   # checking all positions only once
- Space: O(n)   # creating a new list starting from the given one 

"""

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        space = 0
        flowerbed = [0] + flowerbed + [0]

        for i in range(1,len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    space += 1
            if space >= n:
                return True
        return False
