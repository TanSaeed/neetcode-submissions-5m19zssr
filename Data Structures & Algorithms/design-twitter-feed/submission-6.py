class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for follower in self.followMap[userId]:
            if follower in self.tweetMap:
                index = len(self.tweetMap[follower]) - 1
                count, twId = self.tweetMap[follower][index]
                minHeap.append([count, twId, follower, index - 1])

        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, twId, follower, index = heapq.heappop(minHeap)
            res.append(twId)
            if index >= 0:
                count, twId = self.tweetMap[follower][index]
                heapq.heappush(minHeap, [count, twId, follower, index - 1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
