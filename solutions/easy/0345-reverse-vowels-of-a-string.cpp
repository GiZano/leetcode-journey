/*
Problem: 345. Reverse Vowels of a String
Category: Two Pointers

Description: Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Algorithm:
- Set two pointers, one at the end and one at the start of the string
- Iterate until start isn't greater or equal to end
- Scan using the start pointer until a vowel is found
- After that scan backwards using the end pointer until another vowel is found
- Swap the two vowels
- Restart until all vowels are swapped

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
#include <string_view>

using namespace std;

class Solution {
public:
    bool isVowel(char c){
        constexpr string_view vowels = "aeiouAEIOU";
        return vowels.find(c) != string_view::npos;
    }

    string reverseVowels(string s) {
        int start = 0;
        int end = (int)(s.length()) - 1;

        while(start < end){
            if(isVowel(s[start])){
                if(isVowel(s[end])){

                    swap(s[start], s[end]);
                    end--;
                    start++;

                }else{
                    end--;
                }
            }else{
                start++;
            } 
        }
        return s;
    }
};
