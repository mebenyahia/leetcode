'''
Simple fixed size sliding window
Runtime: 31 ms, faster than 93.63% of Python3 online submissions for Find the K-Beauty of a Number.
'''
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        return sum([1 for i in range(len(str(num))-k+1) if int(str(num)[i:i+k]) != 0 and  num % int(str(num)[i:i+k]) == 0])