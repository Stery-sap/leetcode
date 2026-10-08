class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = (total + 1) // 2 
        if len(B) < len(A):
            A, B = B, A     
        low, high = 0, len(A)
        while low <= high:
            i = (low + high) // 2
            j = half - i
            A_left_max = A[i - 1] if i > 0 else float('-inf')
            A_right_min = A[i] if i < len(A) else float('inf')
            B_left_max = B[j - 1] if j > 0 else float('-inf')
            B_right_min = B[j] if j < len(B) else float('inf')
            if A_left_max <= B_right_min and B_left_max <= A_right_min:
                if total % 2 != 0:
                    return float(max(A_left_max, B_left_max))
                return (max(A_left_max, B_left_max) + min(A_right_min, B_right_min)) / 2.0
            elif A_left_max > B_right_min:
                high = i - 1
            else:
                low = i + 1
