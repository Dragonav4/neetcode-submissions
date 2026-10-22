class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)-1
        i=0
        reach_I=0
        while(i <= n): # 0 < 5
            if i > reach_I: return False
            reach_I=max(reach_I,i + nums[i]) # 0 + 1
            if reach_I >= n: return True
            else: i+=1
        return False