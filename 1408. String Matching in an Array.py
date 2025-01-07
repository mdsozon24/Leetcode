class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for s in words:
            for c in words:
                if  s!=c and c in s:
                    ans.add(c)
        return list(ans)