class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        if not s1 and not s2 and not s3:
            return True
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        for i in range(1, len(s1)+1):
            dp[i][0] = s1[:i] == s3[:i]
        for i in range(1, len(s2)+1):
            dp[0][i] = s2[:i] == s3[:i]

        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if (s1[i-1] == s3[i+j-1] and dp[i-1][j]) or (s2[j-1] == s3[i+j-1] and dp[i][j-1]):
                    dp[i][j] = True
        
        return dp[len(s1)][len(s2)]

