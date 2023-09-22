"""
55. Jump Game
You are given an integer array nums. 
You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump 
length at that position.

Return true if you can reach the last index, 
or false otherwise.
"""
"""
First iteration: check for every 0, and upon finding a zero,
see if you can jump over it by checking all the indexes beforehand.
"""
def canJump(nums: list[int]) -> bool:
    if nums.count(0) == 0 or len(nums) == 1:
        return True
    for index in range(len(nums)-1):
        if nums[index] == 0:
            jump = 2
            for index2 in range(index-1,0,-1):
                if jump <= nums[index2]:
                    break
            return False
    return True

"""
Iteration 2 uses a different algorithm, where we
find the max jump range from all the indexes before
zeroes. If the max jump is not over the index of the 0,
return false. The check inbetween checks if the max jump
is also at the end of the list.
"""
def canJump2( nums: list[int]) -> bool:
    maxIndex = 0
    for index in range(len(nums)):
        if nums[index] != 0:
            if index + nums[index] > maxIndex:
                maxIndex = index + nums[index]
        elif maxIndex > index or maxIndex == len(nums)-1:
            continue
        else:
            return False
    return True

canJump2([3,2,1,0,4])
canJump2([0])