class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def recur(arr,cur,su,tar):
            if su > tar:
                return 
            elif su == tar:
                a = sorted(cur)
                if a not in ret:
                    ret.append(a)
                return
            else:
                for num in arr:
                    c = cur.copy()
                    if num > target:
                        continue
                    elif su+num <= target:
                        c.append(num)
                        s = su + num
                        recur(arr,c,s,tar)
        recur(candidates,[],0,target)
        return ret
                        