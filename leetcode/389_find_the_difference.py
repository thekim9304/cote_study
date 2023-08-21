class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for alpha in (t):
            if s.count(alpha) != t.count(alpha):
                return alpha