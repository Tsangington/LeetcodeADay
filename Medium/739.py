"""
739. Daily Temperatures

Given an array of integers temperatures represents the 
daily temperatures, return an array answer such that answer[i]
is the number of days you have to wait after the ith day to get
a warmer temperature. If there is no future day for which 
this is possible, keep answer[i] == 0 instead.
"""
"""
Iteration 1: Ended with time limit exceeded... 
Next idea will be a flag of some kind for the local largest???
"""
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    out = []
    for tempIndex in range(len(temperatures)):
        index = tempIndex+1
        startTemp = temperatures[tempIndex]
        days = 0
        future = False
        while index < len(temperatures):
            if startTemp < temperatures[index]:
                days += 1
                future = True
                break
            else:
                future = False
                days += 1
                index += 1
        if future == True:
            out.append(days)
        else:
            out.append(0)
    return out

dailyTemperatures([73,74,75,71,69,72,76,73])