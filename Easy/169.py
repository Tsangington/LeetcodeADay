"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""


def majorityElement(nums):
    existing = []
    lenDict = {}
    for index in range(len(nums)):
        if nums[index] in existing:
            lenDict[nums[index]] += 1
        else:
            lenDict[nums[index]] = 1
            existing.append(nums[index])
        return (max(lenDict, key=lambda key: lenDict[key]))

result = majorityElement(nums = [3,2,3])
print(result)