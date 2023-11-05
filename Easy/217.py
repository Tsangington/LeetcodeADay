"""
217. Contains Duplicate

Given an integer array nums, return true if any
value appears at least twice in the array, and 
return false if every element is distinct.
"""
def containsDuplicate(nums: list[int]) -> bool:
    unique = set(nums)
    if len(nums) > len(unique):
        return True
    return False

assert(containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]) == True)
