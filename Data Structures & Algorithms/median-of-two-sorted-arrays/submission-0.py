class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B): # we want A to be the smaller array
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            i = (r + l) // 2 # pointer for A
            j = half - i - 2 # pointer for B, -1 for the len offset, another -1 for moving the pointer to left of mid

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright: # left portion is good 
                # odd check
                if total % 2: # mods to 0(Even) means if will return a False and not execute, mods 1(Odd) we can return
                    return min(Aright, Bright)
                else: # even
                    return ( max(Aleft, Bleft) + min(Aright, Bright) ) / 2
            elif Aleft > Bright: # left portion was not good, need to adjust, A left element is larger 
                r = i - 1
            else:
                l = i + 1









        