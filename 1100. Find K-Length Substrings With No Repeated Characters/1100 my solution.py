'''
Used Sliding Window Algorithmic mental model
Simply have a deque, rotate and if all elements are unique in window: increment n
There are probably faster ways to do it, but I'm happy I was able to do it as a newbie :D
'''
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        from collections import deque
        
        if k>len(s):
            return 0
        deq = deque(list(s))
        n=0
        for i in range(len(s)-k+1):
            if len(set(list(deq)[:k])) == len(list(deq)[:k]):
                n+= 1
            deq.rotate(-1)
        return n
