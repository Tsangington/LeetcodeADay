"""
347. Top K Frequent Elements
Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.
"""
from collections import defaultdict

def topKFrequent(nums: list[int], k: int) -> list[int]:
    freq_dict = defaultdict(int)
    for num in nums:
        freq_dict[num] += 1
    
    output = []
    for _ in range(k):
        most_freq = max(freq_dict, key= freq_dict.get)
        freq_dict.pop(most_freq)
        output.append(most_freq)
        
    return output

print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))