class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        counter=0
        j=0
        for i in range(n+1):
            j=i
            bit = i & 1
            counter = 0
            while j != 0:
                if j & 1: counter+=1
                j = j >> 1    
            l.append(counter)
        return l