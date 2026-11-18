class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i, 0)+1
        l=sorted(list(d.items()), key=lambda i: i[1], reverse=True)
        a=[]
        for i in range(k):
            a.append(l[i][0])
        return a