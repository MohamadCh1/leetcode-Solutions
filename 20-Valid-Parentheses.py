class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] in "{[(":
            return self.validation(s,[])
        return False

    def validation(self, st: str, l: List[str]) -> bool:
        if len(st)==0:
            return len(l)==0
        if st[0] in "{[(":
            l.append(st[0])
            return self.validation(st[1:], l)
        if st[0] == ")" and l and l[-1] == "(":
            l.pop()
        elif st[0] == "}" and l and l[-1] == "{":
            l.pop()
        elif st[0] == "]" and l and l[-1] == "[":
            l.pop()
        else:
            return False
        return self.validation(st[1:], l)