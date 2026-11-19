class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        start=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d.keys():
            if d.get(i-1, 0)==0:
                start.append(i)
        m=0
        for i in start:
            c,j=0,i
            while d.get(j,0)>0:
                c+=1
                j+=1
            m=max(m,c)
        return m
