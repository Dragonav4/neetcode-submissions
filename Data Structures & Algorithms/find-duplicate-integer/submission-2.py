class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n): # [1,2,3,2,2]
            while(True):
                v=nums[i] # i:0, v: 1
                if nums[v] == v and v != i: return nums[v]
                temp = nums[v] # temp:2
                nums[v] = nums[i] # 2 = 
                nums[i] = temp