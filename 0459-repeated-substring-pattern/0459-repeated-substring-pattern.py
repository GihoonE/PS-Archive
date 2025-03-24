class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss=(s+s)[1:-1]
        return s in ss
