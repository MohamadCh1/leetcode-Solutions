class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s2 = ""
        for i in range(len(s)-1,-1,-1):
            if i==0:
                if s[i] == "-":
                    if -int(s2) < -2147483648 :
                        return 0
                    return -int(s2)
            if s2 == "" and s[i]==0:
                continue
            s2 = s2 + s[i]
        s2 = int(s2)    
        if s2 < -2147483648 or s2 > 2147483648:
            return 0
        return s2
