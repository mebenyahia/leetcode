'''
Best optimization so far
Faster than 89.56% of Python3 online submissions for Find K-Length Substrings With No Repeated Characters.
'''
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        
        if k>len(s):
            return 0
        
        n = 0
        for i in range(len(s)-k+1):
            if len(set(s[i:k+i])) == k:
                n += 1
        return n
