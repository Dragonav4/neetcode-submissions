class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        base = []
        accum = 0
        nums.sort()
        def recursion(i:int,accum:int): #0,0 .... 2,3 t=4
            if accum == target: # 4 == 4?
                accum=0
                res.append(base[:])
                return
            if i == len(nums) or accum + nums[i] > target: return  #4 > 4?
            
            accum+=nums[i] #4
            base.append(nums[i]) #2
            recursion(i,accum) # 0..4
            base.pop()
            accum-=nums[i]
            recursion(i+1,accum)
        recursion(0,accum) 
        return res
            
