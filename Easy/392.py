"""
392. Is Subsequence

Given two strings s and t, return true if s is a 
subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the 
original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters.
 (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

def isSubsequence(s: str, t: str) -> bool:
    for sIndex in range(len(s)):
        try:
                t = t[t.index(s[sIndex])+1:]
        except ValueError:
            return False
    return True


print(isSubsequence(s = "abc", t = "ahbgdc"))
print(isSubsequence(s = "axc", t = "ahbgdc"))
print(isSubsequence(s = "aaaaaa", t = "bbaaaa"))