class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        adj = collections.defaultdict(list) # i : list of points of [cost, node]

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's algo
        res = 0
        visit = set()
        minH = [[0, 0]] # [cost, point]
        while len(visit) < N:
            cost , pt = heapq.heappop(minH)
            if pt in visit:
                continue
            res += cost
            visit.add(pt)
            for neiCost, nei in adj[pt]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])

        return res



        