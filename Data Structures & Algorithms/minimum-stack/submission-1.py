class MinStack:

    def __init__(self):
        self.min = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        elif self.min[-1] >= val:
            self.min.append(val)
            

    def pop(self) -> None:
        if self.min[-1] == self.stack[-1]:
            del self.min[-1]
        
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        
