class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def recur(arr,cur,su,tar):
            c = cur[:]
            if su == tar:
                ans = sorted(c)
                if ans not in ret:
                    ret.append(ans)
            else:
                for num in arr:
                    c = cur[:]
                    if num > target:
                        continue
                    elif su+num <= target:
                        c.append(num)
                        s = su + num
                        recur(arr,c,s,tar)
        recur(candidates,[],0,target)
        return ret
                        