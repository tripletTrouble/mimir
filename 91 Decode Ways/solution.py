# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The test cases are generated so that the answer fits in a 32-bit integer.

#  2121 => 2,1,2,1 | 2,12,1 | 2,1,21 | 21,2,1 | 21,21
# 212 => 2,1,2 | 2, 12 | 21, 2
# 11111 => 1,1,1,1,1 | 1,1,11,1 | 1,1,1,11 | 1,11,1,1 | 1,11,11 | 11,1,1,1 | 11,11,1 | 11,1,11

class Solution:
    def numDecodings(self, s: str) -> int:
        i = len(s)-2

        if s[i] == "0":
            return 0

        res = [0 for _ in s]
        res.append(1)

        res[-2] = int(s[-1] != '0')

        while i>=0:
            if s[i]=='0':
                res[i] = 0
            else:
                res[i] = res[i+1]
                if (s[i]=='1') or (s[i]=='2' and int(s[i+1])<7):
                    res[i] += res[i+2]
            i -= 1

        return res[0]