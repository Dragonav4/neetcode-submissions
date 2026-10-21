class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome_check(l,r) -> str:
            palindrome = ""    
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                palindrome = max(palindrome,s[l:r+1], key=len)   
                l-=1
                r+=1
            return palindrome
        maxx = ""
        for i in range(len(s)):
            odd = palindrome_check(i,i)
            even = palindrome_check(i,i+1)
            maxx = max(maxx,even,odd, key=len)
        return maxx