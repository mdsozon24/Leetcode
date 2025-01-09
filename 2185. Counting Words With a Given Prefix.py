class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        ans = 0
        for word in words:
            if pref == word[:n]:
                ans += 1
        return ans
