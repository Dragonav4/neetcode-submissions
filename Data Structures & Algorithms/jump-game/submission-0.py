class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)-1
        i=0
        reach=0
        while(i <= n): # 0 < 5
            if i > reach: return False
            reach=max(reach,i + nums[i]) # 0 + 1
            if reach >= n: return True
            else: i+=1
        return False
