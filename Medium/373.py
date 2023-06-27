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

print(kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))
print(kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2))

#WIP: Memory Limit Exceeded, 25/35