class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def recur(cur:str,open:int,close:int):
            if len(cur) == 2*n:
                result.append(cur)
                return
            if open < n:
                recur(cur+"(",open+1,close)
            if close < n and open > close:
                recur(cur+")",open,close+1)
        recur("",0,0)
        return result