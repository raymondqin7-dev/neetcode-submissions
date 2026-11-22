from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        q=deque()
        d={')':'(', '}':'{', ']':'['}
        for i in s:
            if i in d.keys():
                if not q:
                    return False
                if q.pop()!=d[i]:
                    return False
            else:
                q.append(i)
        if q:
            return False
        return True