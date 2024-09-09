"""
LC49: Group Anagrams
https://leetcode.com/problems/group-anagrams/description/
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

Explore:
-> can the input be empty : yes

Brainstorm:
-> Approach using hasmap everytime ,  Time compleixt = n * o(n) ,  Space Complexity = o(n)
-> approach using binary reresentation of characters 

Implementation
 APproach 1 : 
 -> iterate through eac hitem 
 -> start the loop from next 




"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]):

        response = defaultdict(list)

        if not strs:
            return response.values()
        # maping the char Chount to list of anagrams

        hashmap = {}

        for word in strs:
            count = [0] * 26
            unicodevalue = 0
            for ch in word:
                count[ord(ch) - ord("a")] += 1

            response[tuple(count)].append(word)

        return response.values()


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print(Solution().groupAnagrams([""]))