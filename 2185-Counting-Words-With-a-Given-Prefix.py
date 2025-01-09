class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        x=0
        for word in words:
            if(word[:len(pref)]==pref):
                x=x+1
        return x