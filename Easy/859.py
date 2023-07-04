#859. Buddy Strings
"""
#2 scenarios for this to be true: s == goal with a duplicate letter,
e.g a, which will be able to be switched, or loop through and find the 
number of differences in the string. If 2 differences, the swap is true.

def buddyStrings(s, goal):
    count = 0
    if s == goal:
        #check for duplicate letters
        for letter in goal:
            if goal.count(letter) == 2:
                return(True)
    else:
        #check for num of differences
        for index in range(len(goal)):
            if s[index] != goal[index]:
                count += 1
        
        if count == 2:
            return(True)
        return(False)

This failed on the 11th testcase, with 
s = 'abcaa'
goal = 'abcbb' since there were 2 differences, but they were not 
transferrable letters. To counteract this, I will use an array instead of 
a counter to keep track of the differences.
"""
def buddyStrings(s, goal):
    differences = []
    if s == goal:
        #check for duplicate letters
        for letter in goal:
            if goal.count(letter) >= 2:
                return(True)
    elif len(s) != len(goal):
        return(False)
    else:
        #check for num of differences
        for index in range(len(goal)):
            if s[index] != goal[index]:
                differences.append([s[index], goal[index]])

        if len(differences) == 2:
        #check if the other
            if differences[0][0] == differences[1][1] and differences[0][1] == differences[1][0]:
                return(True)
        return(False)

print(buddyStrings(s = 'abcbb',goal = 'abcaa'))
