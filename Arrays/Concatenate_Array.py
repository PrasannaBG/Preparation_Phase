def getConcatenation(self, nums):
        # 1929. Concatenation of Array
        # nums = [1,2,1]
        ans = []
        n = len(nums)

        for i in range(0,(n+n)):
            if(i<n):
                ans.append(nums[i])
            else: 
                ans.append(nums[i-n])
        return ans