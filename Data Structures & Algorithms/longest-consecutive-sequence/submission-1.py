class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d=set(nums)
        start=[]
        for i in d:
            if i-1 not in d:
                start.append(i)
        m=0
        for i in start:
            c,j=0,i
            while j in d:
                c+=1
                j+=1
            m=max(m,c)
        return m
