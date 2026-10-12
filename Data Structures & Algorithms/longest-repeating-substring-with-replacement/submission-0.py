class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # if equal -> return sum
        #длина окна − количество самого частого символа ≤ k
        uq = Counter()
        l,best=0,0

        ## AAABABB
        ## 123
        for r in range(len(s)):
            uq[s[r]]+=1
            while(r-l+1 - max(uq.values()) >k):
                uq[s[l]]-=1
                l+=1
            best = max(best, r-l+1)
        return best



