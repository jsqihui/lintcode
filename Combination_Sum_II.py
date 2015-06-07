class Solution:    
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target): 
        # write your code here
        nums = sorted(candidates)
        ret = []
        self.dfs(nums, target, ret)
        return ret
        
    def dfs(self, nums, target, ret, stack=[], pos=0):
        if target == 0:
            if stack not in ret:
                ret.append(stack[:])
            return
        
        for i in range(pos, len(nums)):
            if target >= nums[i]:
                target = target - nums[i]
                stack.append(nums[i])
                self.dfs(nums, target, ret, stack, i+1)
                stack.pop()
                target = target + nums[i]

