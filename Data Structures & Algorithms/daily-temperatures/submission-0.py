from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        c=deque()
        prev=temperatures[0]
        out=[0]*len(temperatures)
        for i,j in enumerate(temperatures):
            if j>prev:
                while c and c[-1][1]<j:
                    d=c.pop()
                    out[d[0]]=i-d[0]
            c.append((i,j))
            prev=j
        return out