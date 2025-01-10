class Solution:
    def scoreOfString(self, s: str) -> int:
        sum=0
        for n in range(0,len(s)-1):
            sum=sum+abs((ord(s[n])-ord(s[n+1])))
        return sum
        