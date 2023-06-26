def totalCost(costs, k, candidates):
    hiringCost = 0
    for x in range(k):
        first = costs[0:candidates]
        last = costs[-candidates:len(costs)]   #find the  lists using int candidates
        firstHire = min(first)  #find lowest cost of each list
        lastHire = min(last)
        if firstHire <= lastHire:
            hiringCost += firstHire
            firstIndex = first.index(firstHire)
            costs.pop(firstIndex)
        elif lastHire < firstHire:
            hiringCost += lastHire
            lastIndex = last.index(lastHire)
            costs.pop(len(costs)-len(last)+lastIndex)
    return hiringCost

print(totalCost(costs = [50,80,34,9,86,20,67,94,65,82,40,79,74,92,84,37,19,16,85,20,79,25,89,55,67,84,3,79,38,16,44,2,54,58], k = 7, candidates = 12))
#end result: WIP - Time limit exceeded on Testcase 133