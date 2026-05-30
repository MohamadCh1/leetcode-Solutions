class Solution:
    def myPow(self, x: float, n: int) -> float:
        s = x  
        return x**n
        if n>0: 
            for i in range(1,n):
                s = s*x
        else:
            for i in range(n,-1,-1):
                s = s/x
        return s
        