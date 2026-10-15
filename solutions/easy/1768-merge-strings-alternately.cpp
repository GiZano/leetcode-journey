/*
Problem: 1768. Merge Strings Alternately
Category: Hash Map / Two Pointers / Sliding Window / Binary Search / DP / Trees / Graphs

Description: You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Algorithm:
- Get the minimum length of the two string
- Append all characters of each string alternatively into a resulting string
- Append the rest of the string starting from the position "minimum length" until the end of the string
- Return the merged string

Complexity:
- Time: O(N + M)
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
    string mergeAlternately(string word1, string word2) {
        string res;
        size_t l1 = word1.size();
        size_t l2 = word2.size();
        size_t min_len = min(l1, l2);

        res.reserve(l1 + l2);

        for(size_t i = 0; i < min_len; ++i){
            res.push_back(word1[i]);
            res.push_back(word2[i]);
        }

        res.append(word1, min_len);
        res.append(word2, min_len);

        return res;
    }
};
