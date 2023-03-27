class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums)>self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k: #for nums that has length shorter than k
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3,[4,5,8,2])
obj.add(3)   # return 4
obj.add(5)   # return 5
obj.add(10)  # return 5
obj.add(9)   # return 8
obj.add(4)   # return 8
