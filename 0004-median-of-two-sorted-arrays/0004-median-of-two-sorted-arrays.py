class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 + nums2
        nums1.sort()
        total = 0
        l = int(len(nums1)/2)
        if len(nums1)%2==0:
            total = nums1[l]+nums1[l-1]
            total = total/2
        else:
            total = nums1[l]
        return total