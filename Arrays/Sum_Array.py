# 1480. Running Sum of 1d Array
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]

def runningSum(self, nums):
        count = 0
        R_Sums = []
        n = len(nums)
        for i in range(n):
            count += nums[i] 
            R_Sums.append(count)
        return R_Sums