class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==0:
            return False
        count={}
        for n in nums:
            count[n]=count.get(n, 0)+1
        return count[max(count, key=count.get)]>1
        