class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        if not digits:
            return [1]
        carrier = 1 
        for i in range(len(digits)):
            index = len(digits) - i - 1
            num = digits[index]
            digits[index] = (num + carrier) % 10
            carrier = (num + carrier) / 10
        
        if carrier:
            return [1] + digits
        else:
            return digits

