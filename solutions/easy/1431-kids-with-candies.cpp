/*
Problem: 1431. Kids With the Greatest Number of Candies
Category: Arrays

Description: Check which kids would have the greatest number of candies if given a determined quantity of candies (extraCandies).

Algorithm:
- Reserve memory for result vector
- Find maximum value of candies
- Check for each candy if the kid at ith position would have more candies with extra or not
- Push each check in the result vector
- Return the result vector

Complexity:
- Time: O(n)
- Space: O(n) // O(1) auxiliary
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
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> result;
        result.reserve(candies.size());
        
        const int maxCandies = *max_element(candies.begin(), candies.end());

        for(int candy : candies){
            result.push_back(candy + extraCandies >= maxCandies);
        }

        return result;
    }
};

/*
Before fixes (LeetCode passed):

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> result;
        
        int max = candies[0];
        for(int i = 1; i < candies.size(); i++){
            if(candies[i] > max){
                max = candies[i];
            }
        }

        for(int i = 0; i < candies.size(); i++){
            result.push_back(candies[i] + extraCandies >= max);
        }

        return result;
    }
};
*/
