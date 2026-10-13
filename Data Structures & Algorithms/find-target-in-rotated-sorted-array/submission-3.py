class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r,mid=0,len(nums)-1,0
        while(l <= r): # 0 < 5 // 3 < 5
            mid = l + (r -l) // 2  # 2 # 4 
            if nums[mid] == target: # 5 > 2? ## 1 > 2?
                return mid
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]: 
                    l = mid+1
                else:
                    r = mid-1
                
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid-1
                else:
                    l = mid+1

        return -1
