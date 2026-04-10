class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num) # Small heap is a max heap (-1 makes it a max heap)
        # also note -1 is needed invert back into its original number

        # make sure every num in small is <= every num in large

        # if small heap and large heap have value, check if small heaps max value is greater than large heaps min value
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # +1 is for in case its even, anything beyond 1 will need to be moved
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1

        if len(self.large) > len(self.small):
            return self.large[0]

        if len(self.large) == len(self.small):
            return (self.large[0] + self.small[0] * -1) / 2
        
        