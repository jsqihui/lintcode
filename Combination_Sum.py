class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        nums = sorted(candidates)
        ret = []
        self.dfs(nums, target, ret)
        return ret
        
    def dfs(self, nums, target, ret, stack=[], pos=0):
        if target == 0:
            ret.append(stack[:])
            return
        
        for i in range(pos, len(nums)):
            if target >= nums[i]:
                target = target - nums[i]
                stack.append(nums[i])
                self.dfs(nums, target, ret, stack, i)
                stack.pop()
                target = target + nums[i]

