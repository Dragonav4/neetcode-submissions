class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        stack = []
        match = {
            "}":"{",
            ")":"(",
            "]":"["}
        #)
        #]
        #(
        #[ ->
        for b in s: #[ [, (, ]
            if b not in '})]': 
                stack.append(b) # [ [,( ]
            else:
                if len(stack) > 0 and match[b] == stack.pop(): # match[ ] ],,, [ == [
                    continue
                else:
                    return False
        return not stack
