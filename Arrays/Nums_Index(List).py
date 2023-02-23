# Code: 1313
# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]

def decompressRLElist(self, nums):
        n = len(nums)
        N = []
        P = 0
        Q = 0
        for i in range(0,n):
            if ((2*i)+1)<=n:
                P = nums[2*i]
                Q = nums[(2*i)+1] 
                for I in range(0,P):
                    N.append(Q)
        return N