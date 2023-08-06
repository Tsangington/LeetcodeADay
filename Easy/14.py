"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
 
"""
def longestCommonPrefix(strs) -> str:
    longestPrefix = ""
    #Use shortest word for no index range errors
    shortestWord = min(strs)
    for index in range(len(shortestWord)):
        for word in strs:
            if word[index] != shortestWord[index]:
                return longestPrefix
        longestPrefix += shortestWord[index] 
    
    return longestPrefix

print(longestCommonPrefix(strs = ["flower","flow","flight"]))
print(longestCommonPrefix(strs = ["dog","racecar","car"]))
