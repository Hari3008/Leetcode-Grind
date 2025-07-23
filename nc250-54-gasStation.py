class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # 2 pointer
        # n = len(gas)
        # L = 0
        # start, end = n - 1, 0
        # tank = gas[start] - cost[start]
        # while start > end:
        #     if tank < 0:
        #         start-=1
        #         tank += gas[start] - cost[start]
        #     else:
        #         tank += gas[end] - cost[end]
        #         end+=1

        # return start if tank >= 0 else -1

        # Greedy approach
        # If the sum of gas is lesser than sum of cost then obviously it cant be possible
        if sum(gas) < sum(cost):
            return -1
        
        res = 0 
        total = 0

        # Keep adding the total until  the total gets to negative, if gets to negative then updtae the starting point
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                res = i + 1
            
        return res
