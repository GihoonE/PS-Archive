class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        for letter in s.rstrip():
            if letter == '(':
                a.append(letter)
            elif letter == '{':
                a.append(letter)
            elif letter == '[':
                a.append(letter)
            elif letter == ')':
                if len(a) == 0 or a[-1] != '(':
                    return False
                else:
                    a.pop()
            elif letter == '}':
                if len(a) == 0 or a[-1] != '{':
                    return False
                else:
                    a.pop()
            elif letter == ']':
                if len(a) == 0 or a[-1] != '[':
                    return False
                else:
                    a.pop()
        if len(a) == 0:
            return True
        else:
            return False