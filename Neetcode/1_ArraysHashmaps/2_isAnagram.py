"""
LC242: Valid Anagram
https://leetcode.com/problems/valid-anagram/description/

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Assumptions:
->can there be an empty string  yes
-> can both string be sam e: yes


Brainstorm:
->  Two hashamps and compare
->  sum of the string unicoded

Implement

Approach 1 :
-> run through each string create a hashamps
-> check if the hashmaps are same
-> return the response
    Time COmpleixty = O(n) + O(n)
    Space Complexity : O(n) + O(n)'

Approach2 :
-> Run theirugh frist array  find the sum of unicode values of string 1
-> find sum of unicode values of string 2
-> if they are same return True else false
-> this is not optimal approach

Aprrach 3:
-> using lisyts
-> you cannot use lsist because the order of characters matters in lists

"""



#approach1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sum1 = 0
        sum2 = 0
        for ch in s:
            sum1+=ord(ch)

        for ch in t:
            sum2+=ord(ch)


        return True if sum1==sum2 else False


# print(Solution().isAnagram(s = "anagram", t = "nagaram")==True)
# print(Solution().isAnagram(s = "rat", t = "car")== False)


#approach2:


class Solution2:
    def isAnagram2(self, s: str, t: str) -> bool:
        # Create dictionaries to store character counts
        count_s = {}
        count_t = {}

        # Update counts for string s
        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1

        # Update counts for string t
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        # Compare the dictionaries
        return count_s == count_t

# Test cases
print(Solution2().isAnagram2(s="anagram", t="nagaram") == True)
print(Solution2().isAnagram2(s="rat", t="car") == False)

