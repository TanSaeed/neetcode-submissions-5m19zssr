class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        res = ["JFK"]

        tickets.sort()

        for start, end in tickets:
            adj[start].append(end)

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True

            if src not in adj:
                return False

            temp = list(adj[src])
            for i, loc in enumerate(temp):
                adj[src].pop(i)
                res.append(loc)

                if dfs(loc) : return res

                adj[src].insert(i, loc)
                res.pop()


        return dfs("JFK")






        