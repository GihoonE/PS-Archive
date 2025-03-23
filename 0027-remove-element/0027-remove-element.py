class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ret = []
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                ret.append(nums[i])
                count += 1
        if count == 0:
            return count
        else:
            nums[:count] = ret
            return count
