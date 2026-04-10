class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True


        adjList = {i:[] for i in range(n)}

        for e1, e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)

            for j in adjList[i]:
                if j == prev:
                    continue

                if not dfs(j, i):
                    return False


            return True


        return dfs(0, -1) and n == len(visit)


                

        
        