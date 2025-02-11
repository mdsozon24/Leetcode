class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stk = []
        n = len(part)
        lst = list(part)
        for c in s:
            stk.append(c)
            if len(stk) >= n and stk[-n:] == lst:
                for _ in range(n):
                    stk.pop()
        return "".join(stk)