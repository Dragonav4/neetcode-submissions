class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # T is O(nlogn) worst case and S is O(n) worst case
        n = len(nums)
        result = []
        for i in range(n - 2): #o(n)
            if (nums[i]) > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r: #O(n)
                if nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[r], nums[l]])
                    while(l<r and nums[l] == nums[l+1]): l+=1
                    l+=1
                    r-=1
        return result #T is O(n^2+nlogn) S
