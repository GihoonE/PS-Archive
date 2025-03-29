class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #1010 11 --> 11
        if (dividend < 0 and divisor <0) or (dividend > 0 and divisor > 0):
            sign = 1
        else:
            sign = -1
        dividend, divisor = abs(dividend),abs(divisor)
        quotient = 0
        while divisor <= dividend:
            shift = 0
            while (divisor << shift) <= dividend:
                shift += 1
            shift -= 1
            dividend -= divisor << shift
            quotient += 1 << shift
        if sign == -1:
            return -quotient
        else:
            return quotient