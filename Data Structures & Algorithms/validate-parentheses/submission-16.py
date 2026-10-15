class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        checker = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        for i in range(len(s)): # "[(])"
            if s[i] in '[{(': # 
                stack.append(s[i]) 
            elif len(stack)>0 and checker[s[i]] == stack.pop():
                continue
            else:
                return False
        return not stack
            


        
            