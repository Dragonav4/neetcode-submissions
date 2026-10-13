class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # mid = len(nums)
        # minn = nums[0]
        # for i in range(mid-1):
        #     # 3,4,5,6,1,2
        #     if(nums[i] < nums[i-1] or nums[i] > nums[i+1]):
        #         minn = min(minn, nums[i+1])
        #         return minn
        #     else:
        #         mid = mid//2
        # return minn
        l,r,mid=0,len(nums)-1,0
        while(l < r):
            mid = l + (r -l) // 2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        return nums[l]


            

                

