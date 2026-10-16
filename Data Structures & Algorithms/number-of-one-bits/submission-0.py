class Solution:
    def hammingWeight(self, n: int) -> int:
        st = bin(n)
        res = 0
        for i in range(len(st)):
            if st[i] == "1":
                res+=1
        return res