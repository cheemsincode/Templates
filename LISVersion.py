# it is finding longest Arithmetic subsequence 

# what is the state for it let's say  
# you are at some i now you want to know how many longest subsequence exist till this point

# here , its little treaky to do that , / 
# at every i you will have different differnce b/w 
# nums[i] - (nums[j] , 0<= j <i) 

# [3 , 6 , 7, 9 , 12]  
# op = 4

# at i == 0 [1{-3:1 , -6: 1} , {6-3= 3:2 } i ==1 val is  2 , ] 
# i == 3 , {1: 1, 4: 1} , 2 
# for 9 , { 2: 1 , 3: 3 ,-6: 1 } 
# we are having 2 d dp  state  
# dp[i][diff] = dp[j][diff] + 1 
# dp[j][diff] += 1

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        dp = {i:Counter() for i in range(len(nums))}  
        res = 1 
        
        for i in range(1,len(nums)):
            for j in range(i): 
                diff = nums[j] - nums[i] 
                if dp[j][diff] == 0: 
                    dp[j][diff] = 1  
                dp[i][diff] = dp[j][diff] + 1 
                res = max(res , dp[i][diff])   
        return res