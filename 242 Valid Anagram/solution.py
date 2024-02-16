class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sA = list(s)
        tA = list(t)
        sA.sort()
        tA.sort()

        return tA == sA
        
