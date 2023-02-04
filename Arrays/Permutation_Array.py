def buildArray(self, nums):
        # nums = [0,2,1,5,3,4]
        # 1920. Build Array from Permutation
        ans = []
        N = len(nums)
        for i in range(0,N):
            if nums[i] < N:
                ans.append(nums[nums[i]]) 
        return ans
