class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l=[]
        for i in range(len(nums)):
            j, k=i, len(nums)-1
            while j<k:
                c=nums[i]+nums[j]+nums[k]
                if c<0:
                    j+=1
                elif c>0:
                    k-=1
                else:
                    if i<j<k:
                        s=[nums[i], nums[j], nums[k]]
                        if s not in l:
                            l.append(s)
                    j+=1
        return l
