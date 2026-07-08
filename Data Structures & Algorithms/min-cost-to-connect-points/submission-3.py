class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        N = len(points)

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1 , N):
                x2, y2 = points[j]
                dis = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dis, j])
                adj[j].append([dis, i])

        res = 0
        visit = set()
        minH = [[0,0]]
        while len(visit) < N:
            cost, pt = heapq.heappop(minH)
            if pt in visit:
                continue
            res += cost
            visit.add(pt)
            for neicost, neipt in adj[pt]:
                if neipt not in visit:
                    heapq.heappush(minH, [neicost,neipt])

        return res


        