class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums: return []
        if len(nums) == 1: return nums[0]
        
        left = 1
        res=[1]*len(nums)
        for i in range(len(nums)): # 1,2,4,6
            res[i] *= left # 1,1,2,8
            left*=nums[i] # 1,2,4
        right = 1
        for i in reversed(range(len(nums))):
            res[i]*=right
            right*=nums[i]
        return res

