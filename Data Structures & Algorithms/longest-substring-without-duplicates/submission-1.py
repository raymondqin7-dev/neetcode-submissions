class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l={}
        left, best=0,0
        for right, i in enumerate(s):
            while l.get(i, 0)>0:
                l[s[left]]-=1
                left+=1
            l[s[right]]=l.get(s[right], 0)+1
            best=max(right-left+1, best)
        return best