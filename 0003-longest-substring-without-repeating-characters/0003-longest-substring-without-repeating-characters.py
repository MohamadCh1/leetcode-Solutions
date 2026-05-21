class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if len(s)==2:
            return 2 if s[0]!=s[1] else 1
        
        counter = 1
        sub = list(s)
        n={sub[0] : 1}
        i=1
        while i < len(sub):
            if sub[i] not in n:
                n[sub[i]] = i+1
                i=i+1
                if counter < len(n):
                    counter = len(n)
            else: 
                i = list(n.values())[0] + 1
                n = {sub[i-1] : i}
        return counter
            