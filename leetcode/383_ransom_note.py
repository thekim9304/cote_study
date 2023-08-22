class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_lst = list(magazine)
        for ch in ransomNote:
            if ch not in magazine_lst:
                return False
            else:
                magazine_lst.remove(ch)

        return True