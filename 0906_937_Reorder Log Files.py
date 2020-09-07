class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def f(log):
            iden, rest = log.split(' ', 1)
            if rest[0].isdigit():
                return (1,)
            else:
                return (0, rest, iden)

        return sorted(logs, key=f)


"""
    sort functions can have a tuple of keys!!!
"""