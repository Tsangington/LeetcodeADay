"""345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string
and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they 
can appear in both lower and upper cases, more than once."""


def reverseVowels(s):
    vowels = ["a","e","i","o","u"]
    vowelIndex = []
    wordVowels = []
    for index in range(len(s)):
        if s[index].lower() in vowels:
            wordVowels.append(s[index])
            vowelIndex.append(index)
    
    j = 0
    for i in range(len(vowelIndex)-1, -1, -1):
        index = vowelIndex[i]
        s = s[:index] +wordVowels[j] + s[index+1:]
        j += 1
    
    return(s)

print(reverseVowels( s= "AeiouUoiea"))