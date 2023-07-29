"""
58. Length of Last Word

Given a string s consisting of words and spaces,
 return the length of the last word in the string.

A word is a maximal substring
 consisting of non-space characters only.
"""

def lengthOfLastWord( s):
    s = s.strip()
    wordArray = s.split(" ")
    return len(wordArray[-1])

result = lengthOfLastWord( s = "Hello World")
print(result)
