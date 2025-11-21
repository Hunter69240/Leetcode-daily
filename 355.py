import heapq
from collections import defaultdict

class Twitter(object):

    def __init__(self):
        # Global counter to assign timestamps to tweets.
        # We use negative numbers so that the latest tweet has the "smallest" count
        # (this helps with minHeap ordering).
        self.count = 0

        # Maps each userId -> list of [count, tweetId].
        # Stores all tweets posted by a user along with their timestamp.
        self.tweetMap = defaultdict(list)

        # Maps each userId -> set of followees (users they follow).
        self.followMap = defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        Post a new tweet from a user.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        # Add this tweet to the user's tweet list with current timestamp.
        self.tweetMap[userId].append([self.count, tweetId])
        
        # Decrement count so newer tweets always have smaller values
        # (ensures heap pops the most recent first).
        self.count -= 1
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        A user's news feed includes tweets posted by:
          - Themselves
          - People they follow
        The 10 most recent tweets are returned in order from newest to oldest.
        :type userId: int
        :rtype: List[int]
        """
        res = []       # List of tweetIds to return
        minHeap = []   # Heap to keep track of most recent tweets

        # A user should always follow themselves
        self.followMap[userId].add(userId)

        # Add the most recent tweet from each followee into the heap
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1  # index of latest tweet
                count, tweetId = self.tweetMap[followeeId][index]
                # Push into heap: [count, tweetId, followeeId, nextIndex]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # Extract up to 10 most recent tweets
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            # If the followee has more tweets, push the next recent one
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        # Prevent error if trying to unfollow someone not followed
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Example usage:
# obj = Twitter()
# obj.postTweet(1, 5)                  # user 1 posts tweet 5
# feed = obj.getNewsFeed(1)            # returns [5]
# obj.follow(1, 2)                     # user 1 follows user 2
# obj.postTweet(2, 6)                  # user 2 posts tweet 6
# feed = obj.getNewsFeed(1)            # returns [6,5]
# obj.unfollow(1, 2)                   # user 1 unfollows user 2
# feed = obj.getNewsFeed(1)            # returns [5]
