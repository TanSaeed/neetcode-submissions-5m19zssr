class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        res = 0
        visit = set()
        minHeap = [(0, k)]

        for s, t, ti in times:
            edges[s].append((t, ti))

        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            res = max(res, time)

            for neinode, neitime in edges[node]:
                if neinode not in visit:
                    heapq.heappush(minHeap, (time + neitime, neinode))

        return res if len(visit) == n else -1