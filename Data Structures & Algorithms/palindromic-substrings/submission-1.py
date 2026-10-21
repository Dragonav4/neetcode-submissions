class Solution:
    def countSubstrings(self, s: str) -> int:
        if s == "": return 0  
        def palindrome_check(l,r) -> int:
            count =0
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                # palindrome = max(palindrome,s[l:r+1], key=len)   
                l-=1
                r+=1
                count +=1
            return count
        summa =0
        for i in range(len(s)):
            odd = palindrome_check(i,i)
            even = palindrome_check(i,i+1)
            summa += odd+even
        return summa
        






