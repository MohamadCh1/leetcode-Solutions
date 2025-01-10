class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for number in nums:
            counter=0
            for num in nums:
                if(number==num):
                    counter= counter + 1
            if (counter==1):
                return number