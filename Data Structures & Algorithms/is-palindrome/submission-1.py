class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s.lower():
            if i in "abcdefghijklmnopqrstuvwxyz0123456789":
                a+=i
        return a==a[::-1]
        