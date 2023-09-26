"""
228. Summary Ranges
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers
 from a to b (inclusive).

Return the smallest sorted list of ranges that 
cover all the numbers in the array exactly. That is,
 each element of nums is covered by exactly one of 
 the ranges, and there is no integer x such that x 
 is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""
def summaryRanges(nums: list[int]) -> list[str]:
    consec = 0
    out = []
    for index in range(len(nums)-1):
        
        if nums[index+1] - nums[index] == 1:
            consec += 1
        else:
            if consec == 0:
                out.append(f"{nums[index]}")
            else:
                out.append(f"{nums[index]-nums[consec]}->{nums[index]}")
            consec = 0
    return out

def summaryRanges2(nums: list[int]) -> list[str]:
    consec = 1
    out = []
    for index in range(1,len(nums),+1):
        
        if nums[index] - nums[index-1] == 1:
            consec += 1
        else:
            if consec == 1:
                out.append(f"{nums[index-1]}")
            else:
                out.append(f"{nums[index-consec]}->{nums[index-1]}")
            consec = 1
    return out

summaryRanges2(nums = [0,1,2,4,5,7])