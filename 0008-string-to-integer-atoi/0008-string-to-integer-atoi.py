class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s)==0:
            return 0
        if s[0].isalpha():
            return 0
        out = ""
        for i in range(0,len(s)):
            if len(out)==0:
                if s[i] in ["+","-"]:
                    out = out + s[i]
                    continue
                elif s[i]==" ":
                    continue
            if s[i].isdigit():
                out = out + s[i]
            else: 
                break 
        if out == "" or out=="-" or out=="+":
            return 0
        out = int(out)
        if out < -2147483648:
            return -2147483648
        if out > 2147483647:
            return 2147483647
        return out 