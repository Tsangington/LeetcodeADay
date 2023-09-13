"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase
letters into lowercase letters and removing all non-alphanumeric
characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, 
or false otherwise.

"""

def isPalindrome(s: str) -> bool:
    alnum = "abcdefghijklmnopqrstuvwxyz1234567890"
    s = s.lower()
    s = list(s)
    string = [letter for letter in s if letter in alnum]
    print(string)
    for index in range(len(string)//2):
        reverseIndex = -index -1
        if string[index] != string[reverseIndex]:
            return False
    return True