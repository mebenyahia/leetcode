'''
runs way faster and is more elegant
'''
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        
        if k>len(s):
            return 0
        n=0
        for i in range(len(s)-k+1):
            if len(set(list(s[i:k+i]))) == len(list(s[i:k+i])):
                n += 1

        return n