"""
383. Ransom Note

Given two strings ransomNote and magazine, return true 
if ransomNote can be constructed by using the letters 
from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

def canConstruct(ransomNote: str, magazine: str) -> bool:
    magazine = list(magazine)
    for letter in ransomNote:
        if letter in magazine:
            magazine.remove(letter)
        else:
            return False
    return True

print(canConstruct(ransomNote = "a", magazine = "b"))