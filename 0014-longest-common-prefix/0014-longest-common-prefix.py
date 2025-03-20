class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        tar = min(strs,key=len)
        for i,char in enumerate(tar):
            for word in strs:
                if word[i] != char:
                    return ret
            ret += char
        return ret