class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        # Write your code here
        if not a:
            return b
        if not b:
            return a

        carrier = 0
        i = len(a) - 1
        j = len(b) - 1
        ret = ""
        while i >= 0 and j >= 0:
            if a[i] == '1' and b[j] == '1':
                if carrier == 1:
                    ret = '1' + ret
                else:
                    ret = '0' + ret
                carrier = 1
            elif a[i] == '1' or b[j] == '1':
                if carrier == 1:
                    ret = '0' + ret
                    carrier = 1
                else:
                    ret = '1' + ret
                    carrier = 0
            else:
                if carrier == 1:
                    ret = '1' + ret
                else:
                    ret = '0' + ret
                carrier = 0
            i -= 1
            j -= 1
        
        if i < 0:
            while j >= 0:
                if b[j] == '1':
                    if carrier == 1:
                        ret = '0' + ret
                        carrier = 1
                    else:
                        ret = '1' + ret
                        carrier = 0
                else:
                    if carrier == 1:
                        ret = '1' + ret
                    else:
                        ret = '0' + ret
                    carrier = 0
                j -= 1
        if j < 0:
            while i >= 0:
                if a[i] == '1':
                    if carrier == 1:
                        ret = '0' + ret
                        carrier = 1
                    else:
                        ret = '1' + ret
                        carrier = 0
                else:
                    if carrier == 1:
                        ret = '1' + ret
                    else:
                        ret = '0' + ret
                    carrier = 0
                i -= 1
        if carrier == 1:
            ret = '1' + ret
        return ret

