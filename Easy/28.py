"""
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the 
index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

"""
def strStr(haystack: str, needle: str) -> int:
    for index in range(len(haystack)):
        if haystack[index] == needle[0]:
            if haystack[index: index + len(needle)] == needle:
                return (index)
    return (-1)

print(strStr(haystack = "sadbutsad", needle = "sad"))
print(strStr(haystack = "leetcode", needle = "leeto"))