class Solution:
    def romanToInt(self, s: str) -> int:
        let = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        sum = 0
        for i in range(len(s)):
            if i > 0 and let[s[i]] > let[s[i-1]]:
                sum += let[s[i]] - 2*let[s[i-1]]
            else:
                sum += let[s[i]]
        return sum