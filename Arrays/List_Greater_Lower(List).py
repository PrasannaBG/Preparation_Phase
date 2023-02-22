# Code: 1365
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        N = []
        C = 0
        n = len(nums)
        for i in nums:
            for j in range(0,n):
                if (i>nums[j]):
                    C = C + 1
            N.append(C)
            C = 0
        return N
