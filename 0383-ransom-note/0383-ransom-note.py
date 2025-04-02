class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            let = ransomNote[i]
            if let not in magazine:
                return False
            else:
                magazine = magazine.replace(let,'',1)
        return True