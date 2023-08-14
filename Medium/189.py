"""
189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps,
 where k is non-negative.
"""
def rotate(nums: list[int], k: int) -> None:
# added line below for testcases which was longer than the length of the
# array to reduce the splicing needed
    k = k%len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return(nums)

print(rotate(nums = [1,2,3,4,5,6,7], k = 3))