class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxEndingSum = res = nums[0]
        for i in range(1,len(nums)):  # 0
            old_window = maxEndingSum+nums[i] # 
            maxEndingSum = max(nums[i],old_window) # 7
            res = max(res,maxEndingSum) # 7
        return res
            

