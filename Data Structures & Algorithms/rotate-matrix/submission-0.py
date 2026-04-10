class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        l, r = 0, len(matrix[0]) - 1 # -1 because it makes it easier to calc

        while l < r:
            for i in range(r - l):
                t, b = l, r

                # Save Top Left Value
                topL = matrix[t][l+i]

                # Bottom Left into Top Left
                matrix[t][l+i] = matrix[b-i][l]

                # Bottom Right into Bottom Left
                matrix[b-i][l] = matrix[b][r-i]

                # Top Right into Bottom Right
                matrix[b][r-i] = matrix[t+i][r]

                # Top left into Top Right
                matrix[t+i][r] = topL

            # Now that the outer loop is done, we decrement to do the sub problem
            r -= 1
            l += 1



        