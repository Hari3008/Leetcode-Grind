class Twitter:
    # Max Heap
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId : [count, tweetID]
        self.followMap = defaultdict(set) # userID : set of followeeID

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # Store the recent tweet IDs
        minHeap = []

        self.followMap[userId].add(userId) # Add the user itself since you wanna return their tweets too
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1 # index of the recent tweet for the user
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap,[count, tweetId, followeeId, index - 1]) # Push it to heap with the count tweetId and also the previous index so that next time we are able to retrive the next tweet in the heap
        
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap) # Extract the most recent on the heap
            res.append(tweetId)
            if index >= 0: # If there are more tweets for that followeeID, then push the next recent tweet onto the heap with the same indexing logic
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap,[count, tweetId, followeeId, index - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
