class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = {}
        left = 0
        max_len = 0
        for i in range(len(s)):
            cur = s[i]

            if cur in last and last[cur] >= left:
                left = last[cur]+1
            
            last[cur] = i
            max_len = max(max_len, last[cur] - left + 1)
        return max_len
            