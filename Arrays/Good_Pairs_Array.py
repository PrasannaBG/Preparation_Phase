# 1512. Number of Good Pairs
# IN - nums = [1,2,3,1,1,3], OUT - 4

def numIdenticalPairs(self, nums):
        count = 0
        n = len(nums)
        for i in range(0,n):
            for j in range(0,n):
                if (nums[i] == nums[j]) & (i < j):
                    count = count + 1
        return count