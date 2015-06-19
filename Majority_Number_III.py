class Solution:
    """
    @param nums: A list of integers
    @param k: As described
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        hash = {}
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]] += 1
                continue
            if len(hash) == k:
                for key in hash.keys():
                    hash[key] = hash[key] - 1
                    if hash[key] == 0:
                        hash.pop(key)
            else:
                hash[nums[i]] = 1
        
        for key in hash:
            hash[key] = 0
        
        ret = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]] += 1
                if hash[nums[i]] > count:
                    count = hash[nums[i]]
                    ret = nums[i]
        
        return ret
                    

