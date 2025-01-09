class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=0
        y=1
        for number in nums:
            y=x+1
            for num in nums[x+1:]:
                if (number+num==target):
                    return [x,y]
                y=y+1
            x=x+1



        