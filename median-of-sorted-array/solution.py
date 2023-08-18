from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2

        if len(A) > len(B):
            B, A = nums1, nums2


        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A) - 1
        while True:
            i = (l+r) // 2
            j = half - i - 2
            a_left = A[i] if i >= 0 else float("-infinity")
            a_right = A[i + 1] if (i + 1) < len(A) else float("infinity")
            b_left = B[j] if j >=0 else float("-infinity")
            b_right = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if ( a_left <= b_right and b_left <= a_right):
                # found the median
                if ( total % 2 ):
                    # odd number
                    return min(a_right, b_right)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2

            elif a_left > b_right:
                r = i - 1
            else:
                l = i + 1



