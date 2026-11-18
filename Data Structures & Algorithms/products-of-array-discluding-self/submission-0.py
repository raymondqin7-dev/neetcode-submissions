class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        p, s=[0]*n, [0]*n
        p[0]=nums[0]
        s[n-1]=nums[n-1]
        for i in range(1, n):
            p[i]=p[i-1]*nums[i]
            s[n-1-i]=s[n-i]*nums[n-1-i]
        out=[0]*n
        for i in range(1, n-1):
            out[i]=p[i-1]*s[i+1]
        out[0]=s[1]
        out[n-1]=p[n-2]
        return out