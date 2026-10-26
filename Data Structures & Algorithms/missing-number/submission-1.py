class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        init = [i for i in range(len(nums), -1, -1)]
        res=0
        for i in range(len(nums)):
            res ^= init[i] ^ nums[i]
        return res