class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        m = len(nums1)
        if m%2 == 0:
           i = m//2
           j = i-1
           return (nums1[i]+nums1[j])/2
        else:
            return nums1[m//2]
