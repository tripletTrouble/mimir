class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        i = 0
        res = ""

        while i<numRows:
            j=i

            while j<len(s):
                res += s[j]
                n = j+ numRows + (numRows-2)

                if i>0 and i<numRows-1:
                    ix = n-i*2

                    if ix<len(s):
                        res+=s[ix]

                j=n

            i+=1
            
        return res
