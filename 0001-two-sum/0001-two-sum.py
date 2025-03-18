class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = {}
        for ind, num in enumerate(nums):
            tar = target-num
            if tar in ret.keys():
                return [ind,ret[tar]]
            ret[num] = ind