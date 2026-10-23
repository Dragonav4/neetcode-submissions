class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n==2: return n
        curr=0
        prev=1
        prev2=1
        for i in range(1,n):
            curr=prev+prev2
            prev2=prev
            prev=curr
        return curr

            