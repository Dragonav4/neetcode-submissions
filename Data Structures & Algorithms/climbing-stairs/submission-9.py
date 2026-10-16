class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        res = self.recursion(d,n)
        return res

    def recursion(self,d,n) -> int:
        if n == 1 or n == 2: return n # 4
        if n != 0 and n not in d: 
            d[n] = self.recursion(d,n-1) + self.recursion(d,n-2)
        return d[n]

