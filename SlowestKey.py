class Solution:
    def slowestKey(self, releaseTimes, keysPressed: str) -> str:
        slowestInter = 0
        slowestChar = ""
        for i in range(len(releaseTimes)):
            if i==0:
                interval = releaseTimes[i]-0
            else:
                interval = releaseTimes[i]-releaseTimes[i-1]
            if interval>slowestInter:
                slowestInter = interval
                slowestChar = keysPressed[i]
            if interval==slowestInter and keysPressed[i]>slowestChar:
                slowestChar = keysPressed[i]
        return slowestChar

sol = Solution()
print(sol.slowestKey([9,29,49,50], "cbcd"))