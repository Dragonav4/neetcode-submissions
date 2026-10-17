class MinStack:

    def __init__(self): # LIFO
        self.stack = [] # 1,2
        self.min_stack = [] # 1,1
    def push(self, val: int) -> None: 
        self.stack.append(val) # 1,2,0
        if not self.min_stack:
            self.min_stack.append(val) # 0
            return
        top_min_stack = self.min_stack[-1] # 1
        if val >= top_min_stack: # 1 >= 1, 2 >=1?, 0 >= 1
            self.min_stack.append(top_min_stack) #1
        else:
            self.min_stack.append(val) # 0

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
