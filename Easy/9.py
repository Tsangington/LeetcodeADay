"""
9. Palindrome Number

Given an integer x, return true if x is a 
palindrome, and false otherwise.
"""

def isPalindrome(x: int) -> bool:
    x = str(x)
    for index in range(len(x)//2):
        reverseIndex = -index -1
        if x[index] != x[reverseIndex]:
            return False
    return True