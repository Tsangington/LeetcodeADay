"""
202. Happy Number
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the
 sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay),
 or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""
class Solution:
    def isHappy( n: int) -> bool:
        values = []
        while n != 1:
            if squareDigits(n) in values:
                return(False)
            else:
                values.append(n)
            n = squareDigits(n)
        return(True)

def squareDigits(num):
    num = list(str(num))
    add = 0
    for x in num:
        add += int(x)**2
    return(add)

print(Solution.isHappy(n = 19))