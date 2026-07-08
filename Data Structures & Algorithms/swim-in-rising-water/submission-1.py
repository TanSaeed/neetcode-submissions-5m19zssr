class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visit.add((0,0))

        while minH:
            val, r, c = heapq.heappop(minH)
            if r == N -1 and c == N -1:
                return val

            for dr, dc in directions:
                row, col = (r+dr), (c+dc)
                if (row < 0 or col < 0 or row >= N or col >= N or (row,col) in visit):
                    continue
                visit.add((row,col))
                heapq.heappush(minH, [max(val, grid[row][col]), row, col])

        