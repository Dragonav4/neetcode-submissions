class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        precomputed = [1]
        for i in reversed(nums[1:]):
            precomputed.append(precomputed[-1] * i)

        acummulated = 1
        for i in range(len(nums)):
            temp = acummulated * precomputed.pop()
            acummulated *= nums[i]
            nums[i] = temp
        
        return nums