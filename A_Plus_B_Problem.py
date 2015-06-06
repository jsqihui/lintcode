class Solution:
    """
    @param a: The first integer
    @param b: The second integer
    @return:  The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here, try to do it without arithmetic operators.
        #while b != 0:
        #    carrier = a & b
        #    a = a ^ b
        #    b = carrier << 1
        #return a
        i = 0;
        res = 0;
        carry = 0;
        while i < 32:
            aa = (a >> i) & 1;
            bb = (b >> i) & 1;
            res |= (aa ^ bb ^ carry) << i
            if (aa == 1 and bb == 1) or ((aa ==1 or bb == 1) and carry == 1):
                carry = 1
            else:
                carry = 0
            i += 1
        return res;
