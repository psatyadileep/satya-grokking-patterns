"""
Given a string ,return teh repsonse skipping the word in the array
"""


def SkipWord(arr, word):
    if not arr:
        return ""

    if arr.startswith(word):
        return SkipWord(arr[len(word):], word)

    return arr[0] + SkipWord(arr[1:], word)

input_string = "hellothere"
word = "hello"

result = SkipWord(input_string, word)
print(result)
