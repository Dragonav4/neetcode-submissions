class Solution:
    def evalRPN(self, tokens: List[str]) -> int: # LIFO
        # 
        stack = []
        for i in tokens: # (1+2)*3)-4 ||| 1,2+,3*,4-
            if i not in ("+","-","*","/"):
                stack.append(int(i)) # 9 4
            else:
                a = stack.pop()
                b = stack.pop()
                match i:
                    case "+":            
                        stack.append(a+b) # 3
                    case "-":
                        stack.append(b-a) # 4 - 9
                    case "*": #3*3 = 9
                        stack.append(a*b)
                    case "/":
                        stack.append(int(b/a))
        return stack.pop()
