"""
80. Remove Duplicates from Sorted Array II

Given an integer array nums sorted in non-decreasing order, 
remove some duplicates in-place such that each unique element 
appears at most twice. The relative order of the elements 
should be kept the same.

Since it is impossible to change the length of the array 
in some languages, you must instead have the result be placed 
in the first part of the array nums. More formally, 
if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result.
 It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots 
of nums.

Do not allocate extra space for another array. You must do this 
by modifying the input array in-place with O(1) extra memory.
"""
def removeDuplicates(nums: list[int]) -> int:
    existing = []
    index = 0
    while index < len(nums):
        if nums[index] in existing:
            if nums.count(nums[index]) > 2:
                nums.remove(nums[index])
            else:
                index += 1
        else:
            existing.append(nums[index])
            index += 1

    return len(nums)

print(removeDuplicates(nums = [1,1,1,2,2,3]))


# Second version - constant memory with no new arrays needed,
# and slightly quicker running time - (9ms)
def removeDuplicates2(nums: list[int]) -> int:
        index = 0
        num = nums[0]
        count = 0
        while index < len(nums):
            if num == nums[index]:
                count += 1
            else:
                count = 1
                num = nums[index]

            if count > 2:
                nums.remove(nums[index])
                count -= 1
                index -= 1
            index += 1    
            
        return len(nums)

print(removeDuplicates2(nums = [1,1,1,2,2,3]))
