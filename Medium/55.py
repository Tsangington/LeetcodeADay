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