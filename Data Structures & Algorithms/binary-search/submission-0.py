class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l!=r:
            if nums[int((l+r)/2)]<target:
                l=int((l+r)/2)+1
                print("l: "+str(l))
            else:
                r=int((l+r)/2)
                print("r: "+str(r))
        if nums[l]==target:
            return l
        else:
            return -1