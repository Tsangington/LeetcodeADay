
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