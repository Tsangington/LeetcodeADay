"""
242. Valid Anagram

Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging 
the letters of a different word or phrase, typically 
using all the original letters exactly once.

"""

# Best O(n) compared to sorting and checking they
# are the same, since sorting would be O(n * log(n))
def isAnagram(s, t):
    lst = []
    lst.extend(t)
    for letter in s:
        if letter in lst:
                lst.remove(letter)
        else:
                return False
    if len(lst) > 0:
            return False
    return True

result = isAnagram(s="anagram", t="nagaram")
print(result)
