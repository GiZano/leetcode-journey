/*
Problem: 151. Reverse Words in a String
Category: Strings / Two Pointers

Description: Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Algorithm:
- Slide through the string to eliminate extra spaces
- Reverse the string (all characters)
- Slide again and reverse each word

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
    string reverseWords(string s) {
        int len = s.length();
        int read = 0;
        int write = 0;
        bool space = false;

        // slide through the string
        while(read < len){
            // if a non-space character is found
            if(s[read] != ' '){
                // if a space or group of spaces has been found earlier, place it in the correct position one single time
                if(space){
                    s[write++] = ' ';
                    space = false;
                }
                // place current character in current writing position
                s[write++] = s[read++];
            }else{
                // if a space is found and we aren't at the start of writing the correct string, mark as a space needs to be added when a new word is encountered
                if(write > 0) space = true;
                read++;
            }
        }

        // resize and reverse the string to remove all extra spaces that would be trailing and reverse characters
        s.resize(write);
        reverse(s.begin(), s.end());

        int word_start = 0;
        len = write;
        for(int word_end = 0; word_end <= len; word_end++){
            // if we are at the end of the string or we find a space, we have to reverse the current word
            if(word_end == len || s[word_end] == ' '){
                reverse(s.begin() + word_start, s.begin() + word_end);
                word_start = word_end+1;
            }
        }

        return s;
    }
};
