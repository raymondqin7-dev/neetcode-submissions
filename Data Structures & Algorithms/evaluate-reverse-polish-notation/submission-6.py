from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        c=deque()
        acc=0
        for i in tokens:
            try:
                c.append(int(i))
            except ValueError:
                d=c.pop()
                e=c.pop()
                if i=="+":
                    acc=e+d
                elif i=="-":
                    acc=e-d
                elif i=="*":
                    acc=e*d
                elif i=="/":
                    acc=int(e/d)
                c.append(acc)
        return acc