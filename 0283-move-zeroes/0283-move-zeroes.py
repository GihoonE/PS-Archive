class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                z_count += 1
            else:
                if z_count == 0:
                    continue
                else:
                    nums[i-z_count] = nums[i]
                    nums[i] = 0
                