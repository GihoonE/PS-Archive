class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = list(s.split(" "))
        ind = len(a)-1
        while ind >= 0:
            if len(a[ind]) >= 1:
                return len(a[ind])
            ind -= 1
        return -1