class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        i = 0
        while i < len(s):
            if s[i] == 'I':
                sum += 1
            elif s[i] == 'V':
                sum += 5
                if i and s[i-1] == 'I':
                    sum -= 2
            elif s[i] == 'X':
                sum += 10
                if i and s[i-1] == 'I':
                    sum -= 2
            elif s[i] == 'L':
                sum += 50
                if i and s[i-1] == 'X':
                    sum -= 20
            elif s[i] == 'C':
                sum += 100
                if i and s[i-1] == 'X':
                    sum -= 20
            elif s[i] == 'D':
                sum += 500
                if i and s[i-1] == 'C':
                    sum -= 200
            else: #M
                sum += 1000
                if i and s[i-1] == 'C':
                    sum -= 200
            i += 1
        return sum
        
