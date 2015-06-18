class Solution:	
    #@param num: A list of non negative integers
    #@return: A string
    def largestNumber(self, num):
        # write your code here
        num = sorted([str(n) for n in num], cmp=self.comparator)
        return "".join(num).lstrip("0") or "0"
    
    def comparator(self, a, b):
        if a + b > b + a:
            return -1
        else:
            return 1

