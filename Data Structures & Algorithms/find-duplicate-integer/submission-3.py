class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast,slow = 0,0
        while(True): # [1,2,3,2,2]
            slow = nums[slow] # 2
            fast = nums[nums[fast]] # 2
            if slow == fast: break #
        slow2=0
        while(True):
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2: return slow
        