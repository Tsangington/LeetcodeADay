"""
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters 
in alternating order, starting with word1. If a string is longer than the other, 
append the additional letters onto the end of the merged string.

Return the merged string.
"""

def mergeAlternately(word1, word2):
    # find min len
    if len(word1) < len(word2):
        iterations = len(word1)
        endstring = word2[len(word1):]
    else:
        iterations = len(word2)
        endstring = word1[len(word2):]

    mergedString= mergeString(word1, word2, iterations)
    mergedString += endstring

    return (mergedString)
    
def mergeString(word1, word2, iterations):
    mergedString = ""
    for index in range(iterations):
        mergedString += word1[index] + word2[index]
    return(mergedString)

print(mergeAlternately(word1 = "abcd", word2 = "pq"))