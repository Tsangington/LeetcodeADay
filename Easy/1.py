"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    numsDict = {}
    for index in range(len(nums)):
        remainder = target - nums[index]
        if remainder in numsDict:
            return([numsDict[remainder], index]) 
        
        numsDict[nums[index]] = index