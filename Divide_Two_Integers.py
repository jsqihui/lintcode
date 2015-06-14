class Solution:
    # @param {int} dividend the dividend
    # @param {int} divisor the divisor
    # @return {int} the result
    def divide(self, dividend, divisor):
        # Write your code here
        # double the sum then substract from a and renew sum as b
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            if abs(dividend) < abs(divisor):
                return 0
        sum = 0; count = 0; res = 0
        a = abs(dividend); b = abs(divisor)
        while a >= b:
            sum = b
            count = 1
            while sum + sum <= a:
                sum += sum
                count += count
            a -= sum
            res += count
        if dividend >= 2147483647 and divisor == 1:
            return 2147483647
        if dividend <= - 2147483648 and divisor == 1:
            return -2147483648
        if dividend <= - 2147483648 and divisor == -1:
            return 2147483647
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        return res
            

