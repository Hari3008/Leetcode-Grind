class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:


        # Very very interesting question
        # Min Heap

        if len(hand) % groupSize != 0:
            return False
        
        # Hashmap to find the count of the numbers
        count = {}
        for i in hand:
            count[i] = 1 + count.get(i,0)
        
        # Min heapify the count
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        # Keep popping the min element and check if a sequence exists
        while minHeap:
            element = minHeap[0]

            for i in range(element, element + groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i] == 0:
                    if minHeap[0] != i: # if the element is not the minimum of the heap, then return false
                        return False
                    heapq.heappop(minHeap)
        
        return True
