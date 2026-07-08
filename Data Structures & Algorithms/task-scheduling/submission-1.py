class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        ct = Counter(tasks)
        count = [-n for n in ct.values()]
        heapq.heapify(count)

        time = 0
        q = deque()

        while count or q:
            time += 1

            if count:
                data = 1 + heapq.heappop(count)

                if data:
                    q.append([data, time + n])

            if q and q[0][1] == time:
                heapq.heappush(count, q.popleft()[0])

        return time



        