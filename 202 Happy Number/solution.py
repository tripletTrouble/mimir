class Solution:
    def isHappy(self, n: int) -> bool:
        res = []

        while n not in res:
            res.append(n)

            s = str(n)
            ans = 0

            for n in s:
                ans += int(n)**2

            n = ans

        return True if 1 in res else False