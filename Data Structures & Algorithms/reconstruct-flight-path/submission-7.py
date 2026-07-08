class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        res = ["JFK"]
        tickets.sort()

        for start, goto, in tickets:
            adj[start].append(goto)

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, dst in enumerate(temp):
                adj[src].pop(i)
                res.append(dst)

                if dfs(dst) : return res

                adj[src].insert(i, dst)
                res.pop()


        return dfs("JFK")


        




        