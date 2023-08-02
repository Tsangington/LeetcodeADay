"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring
without repeating characters.
"""
def lengthOfLongestSubstring(s):
    existingChars = []
    longestString = ""
    tempLongest = ""
    for index in range(len(s)):
        print(s[index])
        if s[index] in existingChars:
            if len(tempLongest) > len(longestString):
                longestString = tempLongest
            tempLongest = ""
            tempLongest += s[index]
            existingChars = [s[index]]
            print(existingChars, tempLongest)
        else:
            if len(s) == 1:
                return 1
            existingChars.append(s[index])
            tempLongest += s[index]
        if len(tempLongest) > len(longestString):
            longestString = tempLongest
        return len(longestString)
    
def lengthOfLongestSubstring2(s):
    existingChars = []
    longestString = ""
    tempLongest = ""
    for index in range(len(s)):
        if s[index] in existingChars:

            tempLongest = s[index-len(existingChars):index]
            print(existingChars, tempLongest)
            if len(tempLongest) > len(longestString):
                longestString = tempLongest
            tempLongest = s[index]
            existingChars = []
            existingChars.append(s[index])

        else:

            existingChars.append(s[index])

    tempLongest = s[index-len(existingChars):len(s)-1]

    if len(tempLongest) > len(longestString):

        longestString = tempLongest

    return len(longestString)

def lengthOfLongestSubstring3(s):
    existingChars = []
    longestString = ""
    tempLongest = ""
    for index in range(len(s)):
        if s[index] in existingChars:

            tempLongest = s[index-len(existingChars):index]
            print(existingChars, tempLongest)
            if len(tempLongest) > len(longestString):
                longestString = tempLongest
            tempLongest = s[index]
            existingChars = []
            existingChars.append(s[index])

        else:

            existingChars.append(s[index])

    tempLongest = s[index-len(existingChars):len(s)-1]

    if len(tempLongest) > len(longestString):

        longestString = tempLongest

    return len(longestString)

print(lengthOfLongestSubstring2(s = "dvdf"))
print(lengthOfLongestSubstring2(s = "au"))