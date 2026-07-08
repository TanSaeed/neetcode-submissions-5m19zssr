class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        visit = set()

        res = 0

        for u, v, w in times:
            edges[u].append((v, w))

        minHeap =[(0, k)]

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            res = max(res, weight)

            for nei, neiweight in edges[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, (neiweight + weight, nei))

        return res if len(visit) == n else -1

        