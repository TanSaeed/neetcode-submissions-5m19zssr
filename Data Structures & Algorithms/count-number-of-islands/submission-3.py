class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0


        def bfs(r,c):
            q = collections.deque()

            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()

                direct = [[1,0], [-1,0], [0, 1], [0,-1]]

                for dr, dc in direct:
                    if ((row + dr) in range(rows) and
                         (col + dc) in range(cols) and
                         grid[row+dr][ col+dc] == "1" and
                         ((row+dr,col+dc)) not in visit):
                         visit.add((row+dr,col+dc))
                         q.append((row+dr,col+dc))

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == "1":
                    bfs(r,c)
                    island += 1

        return island










        