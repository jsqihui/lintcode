class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        hashcode = 0
        magic = 33
        for c in key:
            hashcode = (hashcode * magic + ord(c)) % HASH_SIZE
        return hashcode

