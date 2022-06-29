'''
Divide and Conquer! with recursion
Runtime beats 95.97 % of python3 submissions.

'''

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        global universalvar 
        universalvar = []
        
        def isasub(s):
            global universalvar
            
            if len(s) == 1 or s == '':
                return
            
            flag = True
            for i in range(len(s)):
                char = s[i].lower() if s[i].isupper() else s[i].upper()
                if char not in s[:i]+s[i+1:]:
                    if s[:i]:
                        isasub(s[:i])
                    if s[i+1:]:
                        isasub(s[i+1:])
                    flag = False
                    break

            if flag and s != None:
                universalvar += [s]

        
        isasub(s)        
        
        return max(universalvar, key=len) if universalvar else ''