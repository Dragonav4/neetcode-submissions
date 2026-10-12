class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        l,best = 0,0
        ##abcabcbb
        for r in range(len(s)):
            while(s[r] in unique): 
                unique.remove(s[l])
                l+=1
            unique.add(s[r])
            best = max(best,len(unique))
        return best
