class Solution:
    def rob(self, nums: List[int]) -> int:
        prev,prev2=0,0
        for i in range(len(nums)):
            maxx = max(nums[i]+prev2,prev)
            prev2 = prev
            prev = maxx
        return prev