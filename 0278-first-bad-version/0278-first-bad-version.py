# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left+right)//2
            print(left,right,mid)
            if isBadVersion(mid):
                right = mid
            else:
                if right-left == 1:
                    left = mid+1
                else:
                    left = mid
        return left