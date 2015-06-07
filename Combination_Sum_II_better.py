class Solution:    
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def __init__(self):
        self.result = []
    
    def combinationSum2(self, candidates, target): 
        # write your code here
        if not candidates:
            return self.result
        nums = sorted(candidates)
        stack = []
        pos = 0
        visited = [False for _ in range(len(nums))]
        self.generate(stack, nums, pos, target, visited)
        return self.result
        
    def generate(self, stack, nums, pos, target, visited):
        if target == 0:
            self.result.append(stack[:])
            return
        elif target < 0:
            return
        for i in range(pos, len(nums)):
            if visited[i] or (i!=0 and not visited[i-1] and nums[i] == nums[i-1]):
                continue
            stack.append(nums[i])
            visited[i] = True
            target = target - nums[i]
            self.generate(stack, nums, i+1, target, visited)
            target = target + nums[i]
            visited[i] = False
            stack.pop()

