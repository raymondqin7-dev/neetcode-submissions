class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j, m=0, len(heights)-1, 0
        while i<j:
            c=min(heights[i], heights[j])*(j-i)
            m=max(m, c)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return m
            