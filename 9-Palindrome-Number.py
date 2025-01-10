class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        else:
            x=str(x) 
            while(len(x)!=1 and len(x)!=0):
                if(x[0] != x[-1]):
                    return False
                x=x[1:len(x)-1]
                
            return True

                

        