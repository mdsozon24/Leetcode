class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        dic = Counter(s)
        ans = 0
        for val in dic.values():
            ans+= (val%2)
            if ans > k:
                return False
        return True