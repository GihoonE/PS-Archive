class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ind = len(digits)-1
        ru = False
        while ind >= 0:
            if ind == len(digits) - 1 or ru:
                if digits[ind] == 9:
                    ru = True
                    digits[ind] = 0
                else:
                    digits[ind] += 1
                    ru = False
            ind -= 1
        if ru:
            digits = [1]+digits
        return digits