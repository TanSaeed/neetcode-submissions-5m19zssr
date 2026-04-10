class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}

        for crs, preq in prerequisites:
            adj[crs].append(preq)

        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if adj[course] == []:
                return True

            visit.add(course)

            for pre in adj[course]:
                if not dfs(pre): return False
            
            visit.remove(course)
            adj[course] = []
            return True



        for i in range(numCourses):
            if not dfs(i): return False

        return True




