class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_value=0
        self.p=[]

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_value=val
        elif val<=self.min_value:
            self.p.append(self.min_value)
            self.min_value=val
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack.pop()==self.min_value and self.p:
            self.min_value=self.p.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value
