class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        res=0
        res = self.recursion(d,n,res)
        return res

    def recursion(self,d,n,res) -> int:
        if n == 1 or n == 2: return n # 4
        if n != 0 and n not in d: 
            d[n] = self.recursion(d,n-1,res) + self.recursion(d,n-2,res)
        return d[n]

