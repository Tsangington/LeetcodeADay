"""
def kSmallestPairs(nums1, nums2, k):
    #create list of all possible outcomes
    pairList = []
    for x in nums1:
        for y in nums2:
            #List is not sorted to sum of the pairs
            pairList.append([x,y])
    #sorting
    pairList = sorted(pairList, key=sum)
    #splice list according to num k
    pairList = pairList[0:k]
    return pairList

#WIP: Memory Limit Exceeded, 25/35

Idea 2: Instead of listing all possible outcomes, calculate sum of arrays,
  and only add to the array if len array is not 3, or smaller than sum.
"""
def kSmallestPairs(nums1, nums2, k):
    pairList = []
    maxPairSum = 0
    for x in nums1:
        for y in nums2:
            total = x+y
            if len(pairList) >= k: #bigger than k means make a check. 
                if total <= maxPairSum:
                    pairList.append([x,y])
            else: #less than 3, find sum of number 
                pairList.append([x,y])
                if total > maxPairSum:
                    maxPairSum = total #change the maxPairSum accordingly so other pairs can be checked.
                                     #When pairList is len 3, this variable should have the biggest sum.
    #sorting
    pairList = sorted(pairList, key=sum)
    #splice list according to num k
    pairList = pairList[0:k]
    return pairList

print(kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))
print(kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2))

#WIP
#New version works, but still exceeds memory limit. Would need to make it change maxSumPair when a smaller array sum is added.