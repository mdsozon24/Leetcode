class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        mp = Counter(s)
        for val in mp.values():
            x = val
            while x > 2:
                n-=2
                x-=2
        return n