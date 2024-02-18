class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sT = s.split(' ')
        if len(pattern) != len(sT):
            return False

        for i in range(len(pattern)):
            if pattern.index(pattern[i]) != sT.index(sT[i]):
                return False

        return True
