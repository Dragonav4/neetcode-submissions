class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures: return []
        stack = [] # LIFO
        l=[0 for i in range(len(temperatures))]
        for i in range(len(temperatures)): # 38
            while(stack and temperatures[i] > temperatures[stack[-1]]):
                j = stack.pop() # 0 
                l[j] = i - j # 1-0
            stack.append(i) #0 , 1
        return l


        

        