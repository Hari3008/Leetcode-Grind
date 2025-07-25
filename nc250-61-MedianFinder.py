class MedianFinder:

    def __init__(self):
        # Maintain 2 heaps
        # Small Heap (Max Heap) which holds the lower values of the array
        # Large Heap (Min Heap) which holds the higher values of the array
        self.smallHeap, self.largeHeap = [], []
 
    def addNum(self, num: int) -> None:

        # Figure out which heap to insert the number into based on the value
        if self.largeHeap and self.smallHeap and num > self.largeHeap[0]:
            heapq.heappush(self.largeHeap, num)
        else:
            heapq.heappush(self.smallHeap, -1 * num)
        
        # Check if the length is almost the same
        if len(self.largeHeap) > len(self.smallHeap) + 1:
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -1 * val)

        if len(self.smallHeap) > len(self.largeHeap) + 1:
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return -1 * self.smallHeap[0]        
        elif len(self.smallHeap) < len(self.largeHeap):
            return self.largeHeap[0]
        else:
            return (-1 * self.smallHeap[0] + self.largeHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
