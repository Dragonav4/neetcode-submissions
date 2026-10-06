class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        result = []
        for i in range(n-2):
            l = i+1
            r=n-1
            while(l<r):
                if(nums[l] + nums[r] + nums[i] < 0):
                    l+=1
                elif(nums[l] + nums[r] +nums[i] > 0):
                    r-=1
                else:
                        if([nums[l],nums[r],nums[i]] in result):
                            r-=1
                            l+=1
                        else:
                            result.append([nums[l],nums[r],nums[i]])
                            r-=1
                            l+=1
        return result


        