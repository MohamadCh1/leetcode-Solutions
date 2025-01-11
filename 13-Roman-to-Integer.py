class Solution:
    def romanToInt(self, s: str) -> int:
        counter = 0
        return self.helper(s, counter) 
    def helper(self  ,st: str,counter: int) -> int:
        if (len(st) == 0):
            return counter
        else:
            match st[0]:
                case "M":
                    counter = counter + 1000
                    return self.helper(st[1:], counter)
                case "C":
                    if (len(st) == 1):
                        return counter + 100
                    if (st[1] == "D"):
                        counter = counter + 400
                        return self.helper(st[2:], counter)
                    elif (st[1] == "M"):
                        counter = counter + 900
                        return self.helper(st[2:], counter)
                    else:
                        counter = counter + 100
                        return self.helper(st[1:],counter)
                case "X":
                    if (len(st) == 1):
                        return counter + 10
                    if (st[1] == "L"):
                        counter = counter + 40
                        return self.helper(st[2:], counter)
                    elif (st[1] == "C"):
                        counter = counter + 90
                        return self.helper(st[2:], counter)
                    else:
                        counter = counter + 10
                        return self.helper(st[1:], counter)
                case "I":
                    if (len(st) == 1):
                        return counter + 1
                    if (st[1] == "V"):
                        counter = counter + 4
                        return self.helper(st[2:], counter)
                    elif (st[1] == "X"):
                        counter = counter + 9
                        return self.helper(st[2:], counter)
                    else:
                        counter = counter + 1
                        return self.helper(st[1:], counter)
                case "V":
                    counter = counter + 5
                    return self.helper(st[1:], counter)
                case "L":
                    counter = counter + 50
                    return self.helper(st[1:], counter)
                case "D":
                    counter = counter + 500
                    return self.helper(st[1:], counter)


