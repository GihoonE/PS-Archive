class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def recur(cur,arr):
            if len(arr) == 1:
                ret.append(cur+arr)
            for i in range(len(arr)):
                a = cur[:]
                a.append(arr[i])
                recur(a,arr[0:i]+arr[i+1:])
        recur([],nums)
        return ret