        ## 对于每一位分别计算k出现在这个位置上有多少个，然后综合相加。对于每一：
        # 如果当前位的数字<k，那么总数是高位个数 -1.
        # 比如153，计算6在个位上出现的个数。因为5<6，所以中间位6可能出现的次数为1*10 (high*base = 10)次。

        #如果当前位==k（我们要寻找k=3），那么除了上面一种情况，还有0-3个

        #如果当前位>k （k=4），那么就是高位都包含了, (high+1)*base = (1+1) * 10 = 20


class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):

        ret = 0
        base = 1
        while n/base > 0:
            cur = (n / base) % 10
            low = n - (n / base) * base
            high = n / (base * 10)
            
            if cur == k:
                ret += high * base + low + 1
            elif cur < k:
                ret += high * base
            else:
                ret += (high + 1) * base
            
            base *= 10
            
        return ret
