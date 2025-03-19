class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            size = 10
            while size <= x:
                size *= 10
            size /= 10

            while x >= 10:
                if x//size != x%10:
                    return False
                else:
                    x %= size
                    x //= 10
                    size /= 100
                    while size > x:
                        if x%10 != 0:
                            return False
                        size /= 100
                        x //= 10
            return True