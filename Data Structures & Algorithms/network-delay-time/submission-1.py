class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        res = 0
        visit = set()
        minHeap = [(0, k)]

        for s, tar, ti in times:
            edges[s].append((tar, ti))

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            
            visit.add(node)
            res = max(res, weight)

            for nodenxt, time in edges[node]:
                if nodenxt not in visit:
                    heapq.heappush(minHeap, (time + weight, nodenxt))

        return res if len(visit) == n else -1



        