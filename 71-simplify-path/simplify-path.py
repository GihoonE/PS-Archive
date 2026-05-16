class Solution:
    def simplifyPath(self, path: str) -> str:
        temp = []
        dirs = list(path.split("/"))
        for word in dirs:
            if word == '.':
                continue
            elif word == '..':
                if temp:
                    temp.pop()
            else:
                if word:
                    temp.append(word)
        return '/'+'/'.join(temp)