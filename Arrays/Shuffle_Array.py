def shuffle(self, nums, n):
        # 1470. Shuffle the Array
        # Input: nums = [2,5,1,3,4,7], n = 3
        # Output: [2,3,5,4,1,7]
         
        nums_1 = nums[:n]
        nums_2 = nums[n:]
        ans = []

        for i in range(0, n):
            ans.append(nums_1[i])
            ans.append(nums_2[i])
        return ans