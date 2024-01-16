'''
Runtime: 69 ms, faster than 75.88% of Python3 online submissions for Unique Email Addresses.
Memory Usage: 14 MB, less than 35.52% of Python3 online submissions for Unique Email Addresses.
'''

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def clean_local(local):
            loc = local.split('+')
            return loc[0].lower().replace('.', '')

        bigls = []
        for e in emails:
            ls = e.split('@')
            if len(ls) == 2:
                bigls.append(''.join([clean_local(ls[0]),'@',ls[1].lower()]))

        return len(set(bigls))
