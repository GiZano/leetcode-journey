/*
Problem: 1071. Greatest Common Divisor of Strings
Category: Math / Strings

Description: For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Algorithm:
- if the concatenation str1 + str2 is equal to str2 + str1 then it has a gcd
- find the gcd of the lengths
- the string gcd is the substring from the position 0 to position length gcd of one of the two strings

Complexity:
- Time: O(N + M)
- Space: O(N + M)
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
    string gcdOfStrings(string str1, string str2) {
        string string_gcd = "";

        if(str1 + str2 == str2 + str1){
            size_t l1 = str1.size();
            size_t l2 = str2.size();
            size_t l_gcd = gcd(l1, l2);
            string_gcd = str1.substr(0, l_gcd);
        }
        return string_gcd;
    }
};

/*
// Alternative with early return:
class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if(str1 + str2 != str2 + str1){
            return "";
        }
        return str1.substr(0, gcd(str1.size(), str2.size()));
    }
};
*/
