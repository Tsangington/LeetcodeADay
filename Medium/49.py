"""
49. Group Anagrams
Given an array of strings strs, 
group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the
letters of a different word or phrase, 
typically using all the original letters exactly once.
"""
from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = list()
    output = []
    for word in strs:
        sorted_word = list(word)
        sorted_word.sort()
        if sorted_word not in anagrams:
            anagrams.append(sorted_word)
            output.append([word])
        else:
            output[anagrams.index(sorted_word)].append(word)
    return output

print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
"""
Second implementation, uses a hashmap to store the data and return the
output list. Also uses a much better sorting algorithm instead of casting
to a list then sorting.
"""
def groupAnagrams2(strs: list[str]) -> list[list[str]]:
    output_dict = defaultdict(list)
    for word in strs:
        output_dict["".join(sorted(word))].append(word)
    
    return list(output_dict.values())