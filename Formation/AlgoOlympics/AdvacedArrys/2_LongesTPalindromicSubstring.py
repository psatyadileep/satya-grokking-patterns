def longest_palindromic_substring(s):
    if not s:
        return ""

    def is_palindrome(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    res = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(i, j):
                if len(res) < j - i + 1:
                    res = s[i:j+1]

    return res

# Test cases
print(longest_palindromic_substring("babe") == "bab")  # True
print(longest_palindromic_substring("abaxyzzyxf") == "xyzzyx")  # True
print(longest_palindromic_substring("it's afternoon") == "noon")  # True
