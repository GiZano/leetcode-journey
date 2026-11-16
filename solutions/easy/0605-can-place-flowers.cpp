/*
Problem: 605. Can Place Flowers
Category: Greedy

Description: Check if it's possible to place 'n' flowers in a flowerbed, counting all space without flowers nearby

Algorithm:
- Iterate over each element
- If at the start or the end count them as 0
- If previous, current and next element are 0es, count one possible flowerbed and increment the counter, if counter is greater or equal to n, return true
- At the end, return wether counter is greater or equal to n

Algorithm (Solution 1):
- First and last position could make problems if the -1 position and size+1 position aren't set as a value, so set them as 0 after reserving space for flowerbed to not encout memory problems
- Iterate over each bed except -1 and size+1
- If previous, current and next are 0es, count one possible flower and set the bed as 1
- Continue
- Check if n is lower or equal to the available flowerbed count

Complexity:
- Time: O(n)
- Space: O(1)
*/

#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <numeric>
#include <queue>
#include <stack>
#include <utility>
#include <climits>

using namespace std;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        // Micro optimization for n == 0 edge case
        if(n == 0){
            return true;
        }

        int count = 0;

        for(size_t i = 0; i < flowerbed.size(); i++){
            // && is lazy in cpp
            if(flowerbed[i] == 0 && (i == 0 ? 0 : flowerbed[i-1]) == 0 && (i == (flowerbed.size()-1) ?  0 : flowerbed[i+1]) == 0){
                    flowerbed[i] = 1;
                    count += 1;
                    if(count >= n){
                        return true;
                    }
            }
        }
        return n <= count;
    }
};

/*

Solution 1 - sentinel padding - passed

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        // Setup flowerbed covering the missing values at start and end, set as 0
        flowerbed.reserve(flowerbed.size() + 2);
        flowerbed.insert(flowerbed.begin(), {0});
        flowerbed.insert(flowerbed.end(), {0});

        int count = 0;
        for(size_t i = 1; i < flowerbed.size()-1; i++){
            // && is lazy in cpp
            if(flowerbed[i] == 0 && flowerbed[i-1] == 0 && flowerbed[i+1] == 0){
                    flowerbed[i] = 1;
                    count += 1;
            }
        }
        return n <= count;
    }
};

*/