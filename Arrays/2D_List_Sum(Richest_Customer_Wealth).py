# 1672. Richest Customer Wealth 
# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6

def maximumWealth(self, accounts):
        
        # Count = []
        # for i in accounts:
        #    Count.append(sum(i))
        # return max(Count)
        
        Max = 0
        for i in range(len(accounts)):
            Sum = 0
            for j in range(len(accounts[i])):
                Sum = Sum + accounts[i][j]
            if Sum > Max:
                Max = Sum
        return Max

'''
Declare a Temp variable to add inner list's numbers and 
check each list sum is greater than max or not in each iteration '''