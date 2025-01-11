class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        st=""
        for i in range(1,len(strs[0])+1):
            s=strs[0][:i]
            for st2 in strs:
                if (s==st2[:i]):
                    continue
                else:
                    return st
            st=s
        return st
            

        