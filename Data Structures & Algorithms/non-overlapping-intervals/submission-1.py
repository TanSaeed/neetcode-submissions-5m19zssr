class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        res = 0
        
        outEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= outEnd:
                outEnd = end
            else:
                res += 1
                outEnd = min(outEnd, end)

        return res
        