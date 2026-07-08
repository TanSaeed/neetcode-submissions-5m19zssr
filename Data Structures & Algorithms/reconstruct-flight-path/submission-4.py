class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True

            if src not in adj:
                return False

            temp = list(adj[src])
            for i, godst in enumerate(temp):
                adj[src].pop(i)
                res.append(godst)

                if dfs(godst): return True

                adj[src].insert(i, godst)
                res.pop()
            return False

        dfs("JFK")
        return res






        