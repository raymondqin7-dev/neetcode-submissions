class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(enumerate(nums), key=lambda i: i[1])
        l=[]
        for i in range(len(nums)):
            j, k=i, len(nums)-1
            while j<k:
                c=nums[i][1]+nums[j][1]+nums[k][1]
                if c<0:
                    j+=1
                elif c>0:
                    k-=1
                else:
                    if i<j<k:
                        l.append([nums[i][1], nums[j][1], nums[k][1]])
                    j+=1
        unique = []
        for i in l:
            if i not in unique:
                unique.append(i)
        return unique
