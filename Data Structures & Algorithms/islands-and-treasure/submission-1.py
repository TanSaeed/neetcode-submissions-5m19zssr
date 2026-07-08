class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        maxA = 0
        visit = set()
        q = deque()

        def chk(r,c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1 or (r,c) in visit):
                return
            visit.add((r,c))
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append([r,c])

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist

                chk(r + 1, c)
                chk(r - 1, c)
                chk(r, c + 1)
                chk(r, c - 1)

            dist += 1





        
        