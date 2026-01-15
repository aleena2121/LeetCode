class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        tank = 0
        total_gas = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_gas += diff
            tank += diff

            if tank < 0:
                start = i + 1
                tank = 0
        
        if total_gas < 0:
            return -1

        return start

