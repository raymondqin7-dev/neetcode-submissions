class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n={}
        for i in strs:
            arr=[0 for _ in range(26)]
            for j in i:
                arr[ord(j)-ord('a')]+=1
            n[tuple(arr)]=n.get(tuple(arr), [])+[i]
        return list(n.values())
        
            