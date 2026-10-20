class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target: return 0
        l,r,m=0,len(nums)-1,0
        while(l < r):
            m = l + (r-l) // 2 # 
            if nums[m] == target: return m
            if nums[m] > target:
                r = m
            else:
                l = m+1
        if nums[l] == target: return l
        return -1