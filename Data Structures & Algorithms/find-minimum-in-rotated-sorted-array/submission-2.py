class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        mid = len(nums)
        minn = nums[0]
        for i in range(mid-1):
            # 3,4,5,6,1,2
            if(nums[i] < nums[i-1] or nums[i] > nums[i+1]):
                minn = min(minn, nums[i+1])
                return minn
            else:
                mid = mid/2
        return minn

            

                

