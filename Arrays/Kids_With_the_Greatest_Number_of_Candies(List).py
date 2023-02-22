# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true]
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        N = []
        for i in candies:
            n = i + extraCandies
            if n >= max(candies):
                N.append(True)
            else:
                N.append(False)
        return N