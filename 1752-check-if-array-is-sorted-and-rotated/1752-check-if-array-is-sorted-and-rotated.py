class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        s=list()
        s2=list()
        for i in range(0,len(nums)-1):
            if nums[i]<=nums[i+1]:
                if (i+1)>=(len(nums)-1):
                    return True
                continue
            else:
                s = nums[:i+1]
                s2= nums[i+1:]
                break
        for i in range(0,len(s2)-1):
            if s2[i]<=s2[i+1]:
                continue
            else:
                return False
        if s2[-1]<=s[0]:
            return True
        else:
            return False

            