class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS , COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            midV = (top + bot) // 2
            if target > matrix[midV][-1]:
                top = midV + 1
            elif target < matrix[midV][0]:
                bot = midV - 1
            else:
                break

            if top > bot:
                return False

        l, r = 0 , COLS - 1

        while l <= r:
            mid = (r + l) // 2
            if target > matrix[midV][mid]:
                l = mid + 1
            elif target < matrix[midV][mid]:
                r = mid - 1
            else:
                return True

        return False

                




        