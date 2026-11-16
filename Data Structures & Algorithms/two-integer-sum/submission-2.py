class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i,j in enumerate(nums):
            a[j]=a.get(j, [])+[i]
            if -j+target != j:
                a[-j+target]=a.get(-j+target, [])+[i]
        return list(dict.fromkeys(max(a.values(), key=len)))
