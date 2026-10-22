class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        maxEndingSum = res = nums[0]
        for i in range(1,len(nums)): 
            maxEndingSum = max(nums[i],maxEndingSum+nums[i]) 
            res = max(res,maxEndingSum) 
        return res
            

