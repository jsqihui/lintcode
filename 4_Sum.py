class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        numLen, res= len(num), set()
        if numLen < 4: return []
        num.sort()
        for i in range(numLen):
            for j in range(i+1, numLen - 2):
                k = j + 1
                l = numLen - 1
                while k < l:
                    s = num[i] + num[j] + num[k] + num[l]
                    if s > target:
                        l -= 1
                    elif s < target:
                        k += 1
                    else:
                        temp = (num[i], num[j], num[k], num[l])
                        if temp not in res:
                            res.add(temp)
                        l -= 1
                        k += 1
        
        return list(res)
                        
                    
