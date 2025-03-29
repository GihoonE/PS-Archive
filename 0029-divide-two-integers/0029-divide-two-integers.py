class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #1010 11 --> 11
        di, div = abs(dividend),abs(divisor)
        quotient = 0
        while div <= di:
            shift = 0
            while (div << shift) <= di:
                shift += 1
            shift -= 1
            di -= div << shift
            quotient += 1 << shift
        if (dividend < 0 and divisor <0) or (dividend > 0 and divisor > 0):
            return min(pow(2,31)-1,quotient)
        else:
            return -quotient