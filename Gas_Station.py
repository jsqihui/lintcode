class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        k = -1
        total_gas = 0
        current_sum = 0
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            current_sum += gas[i] - cost[i]
            if current_sum < 0:
                k = i
                current_sum = 0
        if total_gas >= 0:
            return k + 1
        else:
            return -1

