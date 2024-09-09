"""
LC271:Encode and Decode Strings


Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]
Output: [""]


Approach :
-> The idea is to create a sigle string from the input
-> use the encoded string to decode
-> we wanna make single string by adding the length of each element at the beginning of the word with a pound sign

["Hello","World"] -> 5#HELLO5#WORLD


"

"""


class Codec:
    def encode(self, strs):
        response = ""

        for item in strs:
            response += str(len(item)) + "#" + item

        return response

    def decode(self, s):
        i = 0
        response = []

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
                length = int(s[i:j])
            response.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return response
