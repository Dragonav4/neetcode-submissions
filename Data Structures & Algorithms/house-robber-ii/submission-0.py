class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def rob1(nums):
            prev,prev2=0,0
            for i in range(len(nums)):
                cur = max(nums[i]+prev2, prev)
                prev2=prev
                prev = cur 
            return prev
        return max(rob1(nums[1:]),rob1(nums[:-1]))