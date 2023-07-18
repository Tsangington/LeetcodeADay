"""
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
 and two integers m and n, representing the number of elements in nums1 and nums2 
 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead 
be stored inside the array nums1. To accommodate this, n
ums1 has a length of m + n, where the first m elements denote the elements 
that should be merged, and the last n elements are set to 0 and should be ignored. 
nums2 has a length of n.
"""

def merge(nums1, m, nums2, n):
    i = 0
    for index in range(m+n):
        if nums1[index] == 0:
            if i == n:
                break
            nums1[index] = nums2[i]
            i += 1
    nums1.sort()

print(merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
