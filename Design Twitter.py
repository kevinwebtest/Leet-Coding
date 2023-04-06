class Twitter:

    def __init__(self):
        self.tweetMap = {} #list
        self.followMap = {} #set
        self.latest = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        self.tweetMap[userId].append([self.latest,tweetId])
        self.latest -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        mostRecent = []
        minHeap = []
        if userId not in self.followMap:
            self.followMap[userId] = set()
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]: #get most recent from each followee
            if followeeId in self.tweetMap:
                lastIdx = len(self.tweetMap[followeeId]) - 1
                latest, tweetId = self.tweetMap[followeeId][lastIdx]
                minHeap.append([latest, tweetId, lastIdx-1, followeeId])
        heapq.heapify(minHeap)
        while minHeap and len(mostRecent)<10: #get 10 most recent
            latest, tweetId, lastIdx, followeeId = heapq.heappop(minHeap)
            mostRecent.append(tweetId)
            if lastIdx >= 0:
                latest, tweetId = self.tweetMap[followeeId][lastIdx]
                heapq.heappush(minHeap, [latest, tweetId, lastIdx-1, followeeId])
        return mostRecent

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            if followeeId in self.followMap[followerId]:
                self.followMap[followerId].remove(followeeId)


